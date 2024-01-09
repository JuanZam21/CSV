import csv

with open("weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] == "temp":
            1+1
        else:
            temperatures.append(int(row[1]))
    print(temperatures)