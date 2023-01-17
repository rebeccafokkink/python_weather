#part 1
import json

with open('precipitation.json', encoding = 'utf-8') as file:
    precipitation_file = json.load(file)

seattle_measurements = [measurement for measurement in precipitation_file if measurement['station'] == 'GHCND:US1WAKG0038']
# Create a list of dictionaries with only measurements for Seattle

total_monthly_precipitation = [0,0,0,0,0,0,0,0,0,0,0,0] #initialize list to store total_monthly_precipitation
for measurement in seattle_measurements:    #Go through all the measurements
    date = measurement['date']
    split_date = date.split('-')    #split date into year, month, day
    month = int(split_date[1])  #get month from date
    precipitation = measurement['value']    #value for precipitation
    total_monthly_precipitation[month-1] += precipitation #sum to total precipitation per month

results = {         #create a dictionary with city, state, weather station and total_monthly_precipitation
    "Seattle": {
        "State": "WA",
        "Weather station": "GHCND:US1WAKG0038",
        "Total precipitation per month": total_monthly_precipitation
    }
}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)