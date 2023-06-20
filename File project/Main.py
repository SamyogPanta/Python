import pandas


squirrel_color_list=[]

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]
black_color = 0
red_color = 0
grey_color = 0

for value in color:
    if value == "Gray":
        grey_color += 1
    elif value == "Cinnamon":
        red_color += 1
    elif value == "Black":
        black_color += 1


data_dict = {
    "Fur Color": ["grey_color", "black_color", "red_color"],
    "number": [grey_color,black_color,red_color]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")