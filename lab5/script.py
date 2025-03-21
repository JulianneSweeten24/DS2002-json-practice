#!/usr/bin/env python3
import json
import csv


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


csv_filename = "chacon.csv"

with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "html_url", "updated_at", "visibility"])
        writer.writerows(ext_data[:5]) 
