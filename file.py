from collections import Counter
import csv
from os import read

def mean(total_weight, total_entries):
    mean = total_weight / total_entries
    print(f"Mean (Average) is -> {mean:2f}")


def median(entries,data):
    if entries % 2 == 0:
        median1 = float(data[entries//2])
        median2 = float(data[data//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(data[entries//2])
        print(f"Median is -> {median:2f}")

def mode(data):
    data = Counter(data)

    mode_for_data = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0

    }

    for weight, occurence in data.items():
        if 75 < weight < 85:
            mode_for_data["75-85"] += occurence
        elif 85 < weight < 95:
            mode_for_data["85-95"] += occurence
        elif 95 < weight < 105:
            mode_for_data["95-105"] += occurence
        elif 105 < weight < 115:
            mode_for_data["105-115"] += occurence
        elif 115 < weight < 125:
            mode_for_data["115-125"] += occurence
        elif 125 < weight < 135:
            mode_for_data["125-135"] += occurence
        elif 135 < weight < 145:
            mode_for_data["135-145"] += occurence
        elif 145 < weight < 155:
            mode_for_data["145-155"] += occurence
        elif 155 < weight < 165:
            mode_for_data["155-165"] += occurence
        elif 165 < weight < 175:
            mode_for_data["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_for_data.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")

with open('impStuff.csv') as f:
    reader = csv.reader(f)
    data_files = list(reader)

data_files.pop(0)

weight = 0
entries = len(data_files)
sorted_data = []

for person_data in data_files:
    weight += float(person_data[2])
    sorted_data.append(float(person_data[2]))

sorted_data.sort()

mean(weight, entries)
median(entries, sorted_data)
mode(sorted_data)