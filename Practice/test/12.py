
import csv
import itertools

trigger_mode = [0,1,2,3]

scan_type = ["fast_scan", "full_scan", "customize_scan", "force_scan"]

result = [4,6,3,5,8]

with open("./data.csv", "w", newline="") as f:
    csvWriter = csv.writer(f)
    for i in itertools.product(trigger_mode, scan_type, result):
        data = list(i)
        print(data)
        csvWriter.writerow(data)
