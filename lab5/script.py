#!/usr/bin/env python3
import json
import csv

print("first few steps done")

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

ext_data = []
for repo in data:
        ext_data.append([
                repo.get("name", ""),
                repo.get("html_url", ""),
                repo.get("updated_at", ""),
                repo.get("visibility", "")
        ])

print(f"extraction of {len(ext_data)} repos.")

csv_filename = "chacon.csv"

with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "html_url", "updated_at", "visibility"])
        writer.writerows(ext_data[:5])
print(f"CSV file '{csv_filename}' made")
