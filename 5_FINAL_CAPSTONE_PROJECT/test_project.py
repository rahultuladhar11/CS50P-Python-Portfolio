import pytest
from project import(
    get_threat_level_name,
    format_species_info,
    search_and_add_species,
    Species,
    ConservationDatabase,
    IUCN_API
)

def test_get_threat_level_name():
    assert get_threat_level_name("EX") == "Extinct"
    assert get_threat_level_name("EW") == "Extinct in the Wild"
    assert get_threat_level_name("CR") == "Critically Endangered"
    assert get_threat_level_name("EN") == "Endangered"
    assert get_threat_level_name("VU") == "Vulnerable"
    assert get_threat_level_name("NT") == "Near Threatened"
    assert get_threat_level_name("LC") == "Least Concern"
    assert get_threat_level_name("DD") == "Data Deficient"

    assert get_threat_level_name("XX") == "Unknown"
    assert get_threat_level_name("") == "Unknown"
    assert get_threat_level_name("invalid") == "Unknown"


def test_format_species_info():
    summary = format_species_info(
        common_name="Tiger",
        scientific_name="Panthera tigris",
        kingdom="Animalia",
        category="EN"
    )

    assert "Species: Tiger" in summary
    assert "Scientific Name: Panthera tigris" in summary
    assert "Kingdom: Animalia" in summary
    assert "Conservation Status: Endangered (EN)" in summary


def test_search_and_add_species():
    class Mock_API:
        def search_species(self, name):
            if name == "Panthera tigris":
                return {
                    "main_common_name": "Tiger",
                    "scientific_name": "Panthera tigris",
                    "category": "EN",
                    "kingdom": "Animalia"
                }
            return None

    api_client = Mock_API()
    database = ConservationDatabase()

    search_and_add_species(api_client, database, "Panthera tigris")
    assert database.species_list[0].common_name == "Tiger"
    assert database.species_list[0].scientific_name == "Panthera tigris"
    assert database.species_list[0].category == "EN"
    assert database.species_list[0].kingdom == "Animalia"


def test_species_class():
    tiger = Species("Tiger", "Panthera tigris", "Animalia", "EN")

    assert tiger.common_name == "Tiger"
    assert tiger.scientific_name == "Panthera tigris"
    assert tiger.category == "EN"
    assert tiger.kingdom == "Animalia"

    assert tiger.threatened_status() == True


def test_conservation_database():
    database = ConservationDatabase()

    tiger = Species("Tiger", "Panthera tigris", "Animalia", "EN")
    lion = Species("Lion", "Panthera leo", "Animalia", "VU")
    leopard = Species("Leopard", "Panthera pardus", "Animalia", "VU")
    jaguar = Species("Jaguar", "Panthera onca", "Animalia", "NT")

    database.add_species(tiger)
    database.add_species(lion)
    database.add_species(leopard)
    database.add_species(jaguar)

    threatened = database.get_threatened_list()

    assert len(threatened) == 3
    assert tiger in threatened
    assert lion in threatened
    assert leopard in threatened
    assert jaguar not in threatened

    count = database.count_by_category()

    assert count["EN"] == 1
    assert count["VU"] == 2
    assert count["NT"] == 1

    report = database.generate_report()

    assert "Total species tracked: 4" in report
    assert "No. of threatened species: 3" in report
    assert "Endangered (EN): 1" in report
    assert "Vulnerable (VU): 2" in report
    assert "Near Threatened (NT): 1" in report
