#!/bin/bash
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=$

jq -r '.[].receiptTime' aviation.json | head -n 6

temperature_sum=$(jq -r '[.[].temp] | add' aviation.json)
temperature_count=$(jq -r '[.[].temp] | length' aviation.json)

average_temperature=$(echo "scale=2; $temperature_sum / $temperature_count" | bc)
echo "Average Temperature: $average_temperature"

cloudy_count=$(jq '[.[]|select(.clouds | any(.cover != "CLR"))] | length' aviation.json)

total_reports=$(jq 'length' aviation.json)
half_reports=$((total_reports/2))

if [[ $cloudy_count -gt $half_reports ]]; then
         mostly_cloudy="true"
else
        mostly_cloudy="false"
fi

echo "Mostly cloudy: $mostly_cloudy"
