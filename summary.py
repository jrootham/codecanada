#!/usr/bin/python3

import sys
import csv
import datetime

def collect(row, result):
    name = row["violation_category"]

    values = row["violation_date"].split()[0].split("-")

    year = int(values[0])
    month = int(values[1])
    day = int(values[2])
    timestamp = datetime.date(year, month, day)

    if name in result:
        entry = result[name]
        entry["count"] += 1
        if timestamp < entry["first"]: entry["first"] = timestamp
        if entry["last"] < timestamp: entry["last"] = timestamp
    else:
        entry = {"count": 1, "first": timestamp, "last": timestamp}
        result[name] = entry


def display(result):
    print("Name".ljust(25), "Count".ljust(5), "First".ljust(10), "Last".ljust(10))
    for key in sorted(result.keys()):
        entry = result[key]
        name = key.ljust(25)
        count = str(entry["count"]).rjust(5)
        print(name, count, entry["first"], entry["last"])



#mainline

if 2 != len(sys.argv):
    print("Usage: summary.py file.csv")
else:
    result = {}
    csvfilename = sys.argv[1]
    with open(csvfilename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            collect(row, result)

    display(result)
