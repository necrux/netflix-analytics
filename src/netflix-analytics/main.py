#!/usr/bin/env python3
import pandas
import math

VIEWING_DATA = "../../reports/CONTENT_INTERACTION/ViewingActivity.csv"

data = pandas.read_csv(VIEWING_DATA)
longest_duration = 0

viewing_days = 0
viewing_hours = 0
viewing_minutes = 0
viewing_seconds = 0
for duration in data["Duration"]:
    duration = duration.split(":")
    viewing_hours += int(duration[0])
    viewing_minutes += int(duration[1])
    viewing_seconds += int(duration[2])

viewing_minutes = math.floor(viewing_minutes + (viewing_seconds / 60))
viewing_seconds = viewing_seconds % 60
viewing_hours = math.floor(viewing_hours + (viewing_minutes / 60))
viewing_minutes = viewing_minutes % 60
viewing_days = math.floor(viewing_days + (viewing_hours / 24))
viewing_hours = viewing_hours % 24

print(f"{viewing_days}d {viewing_hours}h {viewing_minutes}m {viewing_seconds}s")
