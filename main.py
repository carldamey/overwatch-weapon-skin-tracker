# import os, csv, pandas

# # def new_data():
# #   data = {    
# #     "comp_points": [0],
# #     "comp_progress": [0],
# #   }

# def save():
#   dataframe = pandas.DataFrame(data)
#   dataframe.to_csv("data.csv", index=False)

# # DETECT SAVE DATA
# if os.path.exists("data.csv"):
#   print("Data Found!")
# else:
#   if input("No Data Found, Create Data File? [Y/N]: ").upper() == "Y":
#     data = {    
#       "comp_points": [int(input("How many competitive points do you have? "))],
#       "comp_progress": [int(input("What is your current competitive progress? "))],
#     }
#     dataframe = pandas.DataFrame(data)
#     dataframe.to_csv("data.csv", index=False)
#   else:
#     print("Okay bye.") 
#     input("")
#     exit

# def save():
#   dataframe = pandas.DataFrame(data)
#   os.remove("data.csv")
#   dataframe.to_csv("data.csv", index=False)

# # read data
# data = pandas.read_csv("data.csv", names=["comp_points", "comp_progress"])
# print(data["comp_points"][1])


# if choice == "A":
#   choice = input("Win [W] or Loss [L]? ").upper()
#   if choice == "W":
#     data["comp_points"][1] = int(data["comp_points"][1]) + 10
#     data["comp_progress"][1] = int(data["comp_points"][1]) + 3
#   elif choice == "L":
#     data["comp_progress"][1] = int(data["comp_progress"][1]) + 1

#   if int(data["comp_progress"][1]) >= 30:
#     data["comp_progress"][1] -= 30
#     data["comp_points"][1] += 100
#   save()
#   choice = ""


# you are % closer

# you are % to jade

# each game is % with n winrate (default 50)

# you need n more wins, each is %

# delete data option

import csv, math, os, pandas

# comp_points = 0
# comp_progress = 0
data = {}

def save():
  dataframe = pandas.DataFrame({
    "comp_points": [data["comp_points"]],
    "comp_progress": [data["comp_progress"]],
  })
  dataframe.to_csv("data.csv", index=False)

def load():
  csv_data = pandas.read_csv("data.csv", names=["comp_points", "comp_progress"])
  return {
    "comp_points": int(csv_data["comp_points"][1]),
    "comp_progress": int(csv_data["comp_progress"][1]),
  }
  
if os.path.exists("data.csv"):
  print("Data Found")

elif not os.path.exists("data.csv"):
  print("No data found, creating data file.")
  data["comp_points"] = input("How many competitive points do you have?\n")
  data["comp_progress"] = input("What is your current competitive progress / 30?\n")
  save()


data = load()
print("Data loaded.", print(data))

while True:
  load()
  print(f"You have {data['comp_points']} Points and {data['comp_progress']} / 30 Progress.")
  primary_choice = input("What would you like to do?\n[A] Add Game\n[V] View Stats\n[U] Update Stats Manually\n[X] Exit Program\n").upper()
  match primary_choice:

    # ADD GAME RESULT
    case "A":
      print("Add Game")
      win_loss_choice = input("Win [W] Loss [L] or Cancel [X]?\n").upper()
      match win_loss_choice:

        # GAME WON
        case "W":
          data["comp_points"] += 10
          data["comp_progress"] += 3
          print("Win logged!")

        # GAME LOST
        case "L":
          data["comp_progress"] += 1
          print("Loss logged. :(")

        # CANCELLED
        case "C":
          print("Canceled")

        # INVALID WIN/LOSS SELECTION
        case _,:
          print("Invalid selection.")

      if data["comp_progress"] >= 30:
        data["comp_progress"] -= 30
        data["comp_points"] += 100
      win_loss_choice = ""
      primary_choice = ""

    case "V":
      print("View Stats")

      print(f"With a 50% win rate, you need to play {math.ceil((3000 - data['comp_points']) / 11.665)} more games.")
      #TODO MAKE THIS MORE ACCURATE BY CALCULATING EXACT PROGRESS

    case "U":
      print("Manually Update Stats")
      

    case "X":
      print("Exit Program")
      break

    case _:
      print("Invalid selection.")

  if data["comp_points"] >= 3000:
    input("Congrats, you now have enough Competitive Points to Purchase your skin! Please make your purchase and then press [ENTER]")
    data["comp_points"] -= 3000

  save()
