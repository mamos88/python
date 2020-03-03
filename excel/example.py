

import openpyxl
from collections import defaultdict

# Documentation: https://openpyxl.readthedocs.io/en/stable/

file_name = r"C:\Users\go_ma\eclipse-workspace\excel\src\foosball.xlsx"

""" Load Workbook """
wb = openpyxl.load_workbook(file_name)

""" Open Sheet """
sheet = wb['Foosball Data']

""" Create Objects to Store Results """
player_dict = defaultdict(int)
shot_dict = defaultdict(int)

""" Read data from columns, count players and goals scored """
for row in range(2, sheet.max_row + 1):
    player = sheet["A" + str(row)].value
    shot = sheet["B" + str(row)].value
    if len(shot) <= 1:
        shot = "Unknown"
    goal = sheet["C" + str(row)].value
    if goal:
        player_dict[player] += 1
        shot_dict[shot] += 1

player_sorted_keys = (sorted(player_dict, key=player_dict.get, reverse=True))
shot_sorted_keys = (sorted(shot_dict, key=shot_dict.get, reverse=True))

""" Create Player Worksheet """
player_sheet = wb.create_sheet('Player Rankings', 1)

player_sheet["A1"].value = "Player"
player_sheet["B1"].value = "Goals Scored"

rownum = 2

""" Populate Player Sheet with Values """ 
for player_key in player_sorted_keys:
    player_sheet["A" + str(rownum)].value = player_key
    player_sheet["B" + str(rownum)].value = player_dict[player_key]
    rownum += 1

""" Create Shots Worksheet """
shot_sheet = wb.create_sheet('Shot Statistics', 2)

shot_sheet["A1"].value = "Shot"
shot_sheet["B1"].value = "Goals Scored"

""" Populate Shot Sheet with Values """ 
rownum = 2
for shot_key in shot_sorted_keys:
    shot_sheet["A" + str(rownum)].value = shot_key
    shot_sheet["B" + str(rownum)].value = shot_dict[shot_key]
    rownum += 1

wb.save(file_name)

print("Finished")













# import openpyxl
# 
# 
# file_name = r"C:\Users\go_ma\eclipse-workspace\excel\src\foosball.xlsx"
# 
# """Loads workbook"""
# wb = openpyxl.load_workbook(file_name)
# 
# """Sets the desired sheet"""
# sheet = wb['Foosball Data']
# 
# """Reads server from column A, looks up the owner in data_from_sysrec and populates column C with owner"""
# for row in range(2, sheet.max_row + 1):
#     server = sheet["A" + str(row)].value
#     try:
#         project_name = server.split("-")[1].split(".")[0]
#     except:
#         pass
#     try:
#         owner = data_from_sysrec[project_name]
#     except KeyError:
#         owner = "Unknown"
#     sheet["C" + str(row)] = owner
#      
# wb.save(file_name)
# 
# print("Finished")