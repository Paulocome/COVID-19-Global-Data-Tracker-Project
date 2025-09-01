 # COVID-19 Global Data Tracker

A Python console application to track COVID-19 data for different countries. The application allows adding, updating, and visualizing confirmed cases, deaths, and recovered patients. Data is saved in a CSV file for persistence, and charts can be generated to visualize the statistics.

## Features

- Add or update COVID-19 data for any country
- View all country data with total statistics
- Generate separate bar charts for confirmed cases, deaths, and recovered patients
- Data is persisted in a CSV file (`covid_data.csv`) to retain information between sessions

## Tools and Libraries

- Python 3.x
- `matplotlib` for charts
- `csv` and `os` modules for file handling
- `datetime` for timestamps

## How to Run

1. Clone or download the repository
2. Install `matplotlib` if not already installed:

```bash
pip install matplotlib

