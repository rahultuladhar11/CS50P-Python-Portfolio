# Wildlife Conservation Tracker

## Video Demo
Add your YouTube video link here

---

## Description

The Wildlife Conservation Tracker is a Python-based application that allows users to search for animal species using their scientific names and retrieve real conservation data from the IUCN Red List API.

The program stores species data in a local database, analyzes their conservation status, and generates a structured report showing biodiversity and threat levels.

This project demonstrates object-oriented programming, API integration, and data processing in Python.

---

## Features

- Search species using scientific (binomial) names (e.g., *Panthera tigris*)
- Fetch real-time data from the IUCN Red List API
- Store multiple species in a local database
- Identify threatened species (CR, EN, VU)
- Count species by conservation category
- Generate a formatted conservation report
- Display detailed summaries of threatened species

---

## Project Structure

### Species Class
Represents a single species and stores:
- Common name
- Scientific name
- Kingdom
- Conservation category

It also includes a method to determine whether a species is threatened.

---

### Conservation Database Class
Manages a collection of species and provides:
- Adding species
- Filtering threatened species
- Counting species by category
- Generating a final conservation report

---

### IUCN API Integration
Handles communication with the IUCN Red List API:
- Retrieves species data using scientific names
- Extracts conservation status and taxonomy
- Handles missing or incomplete data safely

---

## IUCN API Setup

1. Create an account at https://api.iucnredlist.org/
2. Log in to your account
3. Generate an API token from your dashboard
4. Enter the token when the program asks for it

---

## Attribution and Citation

This project uses data from the IUCN Red List of Threatened Species.

Proper citation:
IUCN 2025. IUCN Red List of Threatened Species. Version 2025-2. www.iucnredlist.org

All biodiversity and conservation status data used in this project is derived from this source.

---

## How to Run

### 1. Install dependencies
pip install requests

### 2. Run the program
python project.py

### 3. Follow prompts
- Enter your IUCN API token
- Enter scientific names (e.g., Panthera tigris)
- View generated conservation report

---

## Example Output
=== CONSERVATION REPORT ===

Total species tracked: 4

No. of threatened species: 3

Species by category:

Endangered (EN): 1

Vulnerable (VU): 2

Near Threatened (NT): 1

---

## Design Decisions

- Used object-oriented programming to separate responsibilities (Species, Database, API)
- Used IUCN Red List categories for standardized conservation classification
- Implemented API integration using the `requests` library
- Structured program into modular components for clarity and scalability
- Used helper functions for formatting and category mapping

---

## Notes

- Threatened species are defined as: CR, EN, VU
- NT (Near Threatened) is tracked but not considered threatened
- Requires valid IUCN API token for data access
- Internet connection required for API calls

---

## Author

Name: Rahul Tuladhar

GitHub: rahultuladhar11

edX: rahultuladhar11

Location: Kathmandu, Nepal

Date: May 29 2026
