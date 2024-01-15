# Import library to read CSV files
import pandas as pd

# Open it and logic to read only temperature data
data = pd.read_csv("weather_data.csv")

print(data['temp'])