import os, csv, pandas

# def new_data():
#   data = {    
#     "comp_points": [0],
#     "comp_progress": [0],
#   }

def save():
  dataframe = pandas.DataFrame(data)
  dataframe.to_csv("data.csv", index=False)

# DETECT SAVE DATA
if os.path.exists("data.csv"):
  print("Data Found!")
else:
  if input("No Data Found, Create Data File? [Y/N]: ").upper() == "Y":
    data = {    
      "comp_points": [int(prompt("How many competitive points do you have? "))],
      "comp_progress": [int(prompt("What is your current competitive progress? "))],
    }
    dataframe = pandas.DataFrame(data)
    dataframe.to_csv("data.csv", index=False)
  else:
    print("Okay bye.") 
    input("")
    exit

def save():
  dataframe = pandas.DataFrame(data)
  dataframe.to_csv("data.csv", index=False)

# read data
data = pandas.read_csv("data.csv", names=["comp_points", "comp_progress"])
print(data["comp_points"][1])

# if no data 

# add one game , update progress, update points

# you are % closer 

# you are % to jade

# each game is % with n winrate (default 50)

# you need n more wins, each is %

# delete data option