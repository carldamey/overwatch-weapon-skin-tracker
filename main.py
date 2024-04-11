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
      "comp_points": [int(input("How many competitive points do you have? "))],
      "comp_progress": [int(input("What is your current competitive progress? "))],
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
choice = ""

print("You have", data["comp_points"][1], "competitive points.")
print("You have", data["comp_progress"][1], "/ 30 competitive progress.")
print(f"data - {data}")

while choice != "A":
  choice = input("""What would you like to do? 
  Add Game [A]
  View Stats [V]
  Update Manually [U]
  """).upper()

if choice == "A":
  choice = input("Win [W] or Loss [L]? ").upper()
  if choice == "W":
    data["comp_points"][1] += 10
    data["comp_progress"[1]] += 3
  elif choice == "L":
    data["comp_progress"][1] += 1

  if data["comp_progress"][1] >= 30:
    data["comp_progress"][1] -= 30
    data["comp_points"][1] += 100
  save()
  choice = ""


# you are % closer

# you are % to jade

# each game is % with n winrate (default 50)

# you need n more wins, each is %

# delete data option
