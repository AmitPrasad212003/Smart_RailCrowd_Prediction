import csv
import random
from datetime import datetime, timedelta

# Define parameters
stations = ["New Delhi", "Howrah", "Mumbai CST", "Chennai Central", "Bangalore City"]
platform_numbers = list(range(1, 6))  # Platforms 1 to 5
congestion_levels = ["Low", "Medium", "High"]
peak_hours = ["Morning", "Afternoon", "Evening", "Night"]

# Generate unique timestamps
start_time = datetime.now().replace(minute=0, second=0, microsecond=0)
num_entries = len(stations) * len(platform_numbers)

data = []
for i in range(num_entries):
    timestamp = start_time + timedelta(hours=i//6, minutes=(i%6)*10)  # Varying hours and minutes
    station = random.choice(stations)
    platform = random.choice(platform_numbers)
    platform_footfall = random.randint(500, 2000)
    overall_footfall = random.randint(500, 5000)
    congestion_level = random.choice(congestion_levels)
    entry_count = random.randint(500, 10000)
    exit_count = random.randint(100, 10000)
    peak_hour = random.choice(peak_hours)
    
    data.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), station, platform, platform_footfall, overall_footfall, congestion_level, entry_count, exit_count, peak_hour])

# Write data to CSV
csv_filename = "station_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Station", "Platform", "Platform Footfall", "Overall Footfall", "Congestion Level", "Entry Count", "Exit Count", "Peak Hours"])
    writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully!")
