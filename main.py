# Import library to read CSV files
import csv

# Open it and logic to read only temperature data
with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
