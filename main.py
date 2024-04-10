import os, csv, pandas

# DETECT SAVE DATA
if os.path.exists("data.csv"):
  print("Data Found!")
else:
  if input("No Data Found, Create Data File? [Y/N]: ").upper() == "Y":
      new_data()
      save()
  else:
    print("Okay bye.") 
    input("")
    exit

# read data
data = pandas.read_csv("data.csv")
print(data)

# if no data 

# add one game , update progress, update points

# you are % closer 

# you are % to jade

# each game is % with n winrate (default 50)

# you need n more wins, each is %

# delete data option

def new_data():
  data = {
    "comp_progress": [0],
    "comp_points": [0],
  }

def save():
  dataframe = pandas.DataFrame(data)
  dataframe.to_csv("data.csv", index=False)