import csv
import os
import shutil

import win32api

str = r"D:\OWL\ceshi\owl\scan.bat"
win32api.ShellExecute(0,'open',str,"","D:\\OWL\\ceshi\\owl",0)

# str = r'D:\\tmp\\sample'
# shutil.rmtree(str)
# os.mkdir(str)

# trigger_mode = [0,1,2,3]
#
# scan_type = ["fast_scan", "full_scan", "customize_scan", "force_scan"]
#
# result = [4,6,3,5]
#
# with open("./data.csv", "w", newline="") as f:
#     csvWriter = csv.writer(f)
#     for index1 in range(len(trigger_mode)):
#         for index2 in range(len(scan_type)):
#             for index3 in range(len(result)):
#                 print(trigger_mode[index1], scan_type[index2], result[index3])
#                 csvWriter.writerow([trigger_mode[index1], scan_type[index2], result[index3]])


