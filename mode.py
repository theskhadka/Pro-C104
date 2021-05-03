from collections import Counter
import csv
with open('heightweight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))
data = Counter(new_data)
mode_range = {
    "90-100": 0, 
    "100-110": 0,
    "110-120": 0,
    "120-130": 0,
    "130-140": 0,
    "140-150": 0,
    }
for weight, occurence in data.items():
    if 90<float(weight)<100:
        mode_range["90-100"] += occurence
    elif 100<float(weight)<110:
        mode_range["100-110"] += occurence
    elif 110<float(weight)<120:
        mode_range["110-120"] += occurence
    elif 120<float(weight)<130:
        mode_range["120-130"] += occurence
    elif 130<float(weight)<140:
        mode_range["130-140"] += occurence
    elif 140<float(weight)<150:
        mode_range["140-150"] += occurence
mode_r, mode_occurence = 0, 0
for range, occurence in mode_range.items():
    if occurence>mode_occurence:
        mode_r, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_r[0]+mode_r[1])/2)
print(f"The mode is -> {mode:2f}")