# with open("/day-25/weather-data.csv") as data_file:
#     contents = data_file.readlines()

# import csv

# with open("./day-25/weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data)
# data_list = data["temp"].to_list()
# print(data_list)
# avg = sum(data_list)/len(data_list)
# print(avg)
# print(data["temp"].max())

# # Get data in Row
# print(data[data.day == "Monday"])

# # Row which has highest temp in a week
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
