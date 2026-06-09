import requests
import sys
from typing import List, Dict, Optional

class Species:
    def __init__(self, common_name, scientific_name, kingdom, category):
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.kingdom = kingdom
        self.category = category


    def threatened_status(self):
        return self.category in ["CR", "EN", "VU"]

    def get_summary(self):

        return format_species_info(
            self.common_name,
            self.scientific_name,
            self.kingdom,
            self.category
        )

class ConservationDatabase:

    def __init__(self):
        self.species_list = []

    def add_species(self, species):
        self.species_list.append(species)

    def get_threatened_list(self):
        return [s for s in self.species_list if s.threatened_status()]

    def count_by_category(self):
        categories = {}
        for species in self.species_list:
            cat = species.category
            categories[cat] = categories.get(cat, 0) + 1
        return categories

    def generate_report(self):
        if not self.species_list:
            return "No species data available"

        total = len(self.species_list)
        threatened = len(self.get_threatened_list())
        category_count = self.count_by_category()

        report = f"""
        === CONSERVATION REPORT ===
        Total species tracked: {total}
        No. of threatened species: {threatened}

        Species by category:
        """
        for cat, count in sorted(category_count.items()):
            cat_name = get_threat_level_name(cat)
            report += f"  {cat_name} ({cat}): {count}\n"

        return report


class IUCN_API:

    BASE_URL = "https://api.iucnredlist.org"
    ENDPOINT = "/api/v4/taxa/scientific_name"
    FULL_URL = BASE_URL + ENDPOINT

    def __init__(self, api_token):
        self.api_token = api_token
        self.session = requests.Session()

    def search_species(self, scientific_name):
        try:
            parts = scientific_name.split()
            if len(parts) < 2:
                print(f"Invalid scientific name: {scientific_name}")
                return None
            genus = parts[0]
            species = parts[1]

            params = {"genus_name": genus, "species_name": species}
            headers = {"Authorization": self.api_token}

            response = requests.get(self.FULL_URL, params=params, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("taxon"):
                taxon = data["taxon"]

                common_name = scientific_name
                if taxon.get("common_names") and len(taxon["common_names"]) > 0:
                    for name in taxon["common_names"]:
                        if name.get("language") == "eng":
                            common_name = name.get("name", scientific_name)
                            break

                category = "DD"

                if "assessments" in data and len(data["assessments"]) > 0:
                    for assessment in data["assessments"]:
                        if assessment.get("latest") and assessment.get("scopes"):
                            scope = assessment["scopes"][0]
                            if scope["code"] == "1":
                                category = assessment.get("red_list_category_code", "DD")
                                break

                return {
                    "scientific_name": taxon.get("scientific_name", scientific_name),
                    "main_common_name": common_name,
                    "category": category,
                    "kingdom": taxon.get("kingdom_name", "Unknown")
                }

            return None

        except Exception as e:
            print(f"Error: {e}")
            return None


##################### 3 STANDALONE FUNCTIONS #################################

def get_threat_level_name(category_code):

    levels = {
        "EX": "Extinct",
        "EW": "Extinct in the Wild",
        "CR": "Critically Endangered",
        "EN": "Endangered",
        "VU": "Vulnerable",
        "NT": "Near Threatened",
        "LC": "Least Concern",
        "DD": "Data Deficient"
    }
    return levels.get(category_code, "Unknown")


def format_species_info(common_name, scientific_name, kingdom, category):

    threat_level = get_threat_level_name(category)

    return f"""
            Species: {common_name}
            Scientific Name: {scientific_name}
            Kingdom: {kingdom}
            Conservation Status: {threat_level} ({category})
            """

def search_and_add_species(api_client: IUCN_API, database: ConservationDatabase, species_name: str):

    data = api_client.search_species(species_name)

    if not data:
        print(f"Species '{species_name}' not found")
        return False

    species = Species(
        common_name=data.get("main_common_name", species_name),
        scientific_name=data.get("scientific_name", "Unknown"),
        kingdom=data.get("kingdom", "Unknown"),
        category=data.get("category", "DD")
    )

    database.add_species(species)
    print(f"Added: {species} - Done")
    return True


###############################################################################


def main():
    print("Welcome to Wildife Tracker! 🐅🦁")

    api_token = input("Enter your IUCN API v4 token: ")

    api_client = IUCN_API(api_token)
    database = ConservationDatabase()

    search_list = []

    while True:
        species_name = input("Enter scientific name of species (Eg. Panthera tigris): ")
        search_list.append(species_name)
        add_another = input("Do you wish to search for another species? (Y/N) ")
        if add_another == "N" or add_another =="n":
            break

    for species_name in search_list:
        search_and_add_species(api_client, database, species_name)

    # Display Report
    print()
    print(database.generate_report())

    # Display critically threatened species
    threatened = database.get_threatened_list()
    if threatened:
        print("\n=== THREATENED SPECIES ===")
        for species in threatened:
            print(species.get_summary())


if __name__ == "__main__":
    main()
