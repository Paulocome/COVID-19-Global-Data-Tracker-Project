import datetime
import csv
import os
import matplotlib.pyplot as plt

filename = "covid_data.csv"

def load_data():
    data = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['confirmed'] = int(row['confirmed'])
                row['deaths'] = int(row['deaths'])
                row['recovered'] = int(row['recovered'])
                data.append(row)
    return data

def save_data(data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['country', 'confirmed', 'deaths', 'recovered', 'updated_at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

covid_data = load_data()

def add_or_update_country():
    country = input("Country name: ")
    confirmed = int(input("Confirmed cases: "))
    deaths = int(input("Deaths: "))
    recovered = int(input("Recovered: "))
    updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for entry in covid_data:
        if entry['country'].lower() == country.lower():
            entry['confirmed'] = confirmed
            entry['deaths'] = deaths
            entry['recovered'] = recovered
            entry['updated_at'] = updated_at
            print(f"{country} data updated successfully!\n")
            save_data(covid_data)
            return

    covid_data.append({
        'country': country,
        'confirmed': confirmed,
        'deaths': deaths,
        'recovered': recovered,
        'updated_at': updated_at
    })
    save_data(covid_data)
    print(f"{country} data added successfully!\n")

def show_data():
    if not covid_data:
        print("No data available.\n")
        return

    sorted_data = sorted(covid_data, key=lambda x: x['confirmed'], reverse=True)
    print("\n--- COVID-19 Global Data Tracker ---")
    for entry in sorted_data:
        print(f"Country: {entry['country']}")
        print(f"Confirmed Cases: {entry['confirmed']}")
        print(f"Deaths: {entry['deaths']}")
        print(f"Recovered: {entry['recovered']}")
        print(f"Updated at: {entry['updated_at']}\n")

    total_confirmed = sum(x['confirmed'] for x in covid_data)
    total_deaths = sum(x['deaths'] for x in covid_data)
    total_recovered = sum(x['recovered'] for x in covid_data)
    print(f"Total Confirmed Cases: {total_confirmed}")
    print(f"Total Deaths: {total_deaths}")
    print(f"Total Recovered: {total_recovered}\n")

def plot_data_separate():
    if not covid_data:
        print("No data to plot.\n")
        return

    countries = [x['country'] for x in covid_data]
    confirmed = [x['confirmed'] for x in covid_data]
    deaths = [x['deaths'] for x in covid_data]
    recovered = [x['recovered'] for x in covid_data]

    plt.figure(figsize=(10,6))
    plt.bar(countries, confirmed, color='dodgerblue')
    plt.title("Confirmed Cases by Country")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,6))
    plt.bar(countries, deaths, color='red')
    plt.title("Deaths by Country")
    plt.xlabel("Country")
    plt.ylabel("Deaths")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,6))
    plt.bar(countries, recovered, color='green')
    plt.title("Recovered by Country")
    plt.xlabel("Country")
    plt.ylabel("Recovered")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    print("1. Add or update country data")
    print("2. Show all data")
    print("3. Generate separate charts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_or_update_country()
    elif choice == '2':
        show_data()
    elif choice == '3':
        plot_data_separate()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please try again.\n")
