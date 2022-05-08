
import openpyxl,pprint

# wb = openpyxl.load_workbook("./censuspopdata.xlsx")
# #
# # sheet = wb.get_sheet_by_name("Population by Census Tract")
# #
# # countyData = {}
# #
# # for row in range(2,sheet.max_row + 1):
# #     state = sheet['B' + str(row)].value
# #     country = sheet['C' + str(row)].value
# #     pop = sheet['D' + str(row)].value
# #     countyData.setdefault(state,{})
# #     countyData[state].setdefault(country,{'tracts':0, 'pop':0})
# #     countyData[state][country]['tracts'] += 1
# #     countyData[state][country]['pop'] += int(pop)
# #
# # resultFile = open("result.py",'w')
# # resultFile.write('allData' + pprint.pformat(countyData))
# # resultFile.close()

