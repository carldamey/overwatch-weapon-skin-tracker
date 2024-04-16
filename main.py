import csv, math, os, pandas, random
data = {}
running = True

def save():
  print("DATAafjldshfkjsldfhkjsfh", data)
  dataframe = pandas.DataFrame({
    "comp_points": [data["comp_points"]],
    "comp_progress": [data["comp_progress"]],
  })
  dataframe.to_csv("data.csv", index=False)

def new_data():
  input_data = {
    "comp_points": "",
    "comp_progress": "",
  }
  while not input_data["comp_points"].isdigit():
    input_data["comp_points"] = input("How many competitive points do you have?\n")
  while not input_data["comp_progress"].isdigit():
    input_data["comp_progress"] = input("What is your current competitive progress / 30?\n")
  return input_data

def load():
  if os.path.exists("data.csv"):
    print("Data Found")
  elif not os.path.exists("data.csv"):
    print("No data found, creating data file.")
    data = new_data()
    print("DATAAJDKLSDJLASJD", data)
    save()
  csv_data = pandas.read_csv("data.csv", names=["comp_points", "comp_progress"])
  return {
    "comp_points": int(csv_data["comp_points"][1]),
    "comp_progress": int(csv_data["comp_progress"][1]),
  }

def calculate_games_left(winrate = 50):
  games_needed = 0
  points_needed = 3000 - data["comp_points"]
  calculating_progress = data["comp_progress"]
  while points_needed > 0:
    if winrate > random.randint(1, 100):
      points_needed -= 10
      calculating_progress += 3
    else:
      calculating_progress += 1
    if calculating_progress >= 30:
      points_needed -= 100
      calculating_progress -= 30
    games_needed += 1
  input(f"With a {winrate}% winrate, you will need to play approximately {games_needed} more games, each win bringing you {round((100 / games_needed), 1)}% closer.")

while running:
  data = load()
  print(f"You have {data['comp_points']} Points and {data['comp_progress']} / 30 Progress.")
  primary_choice = input("What would you like to do?\n[A] Add Game\n[V] View Stats\n[U] Update Stats Manually\n[X] Exit Program\n").upper()
  match primary_choice:

    # ADD GAME RESULT
    case "A":
      print("Add Game")
      win_loss_choice = input("[W] Win\n[L] Loss\n[X] Cancel\n").upper()
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

        # CANCELED
        case "X":
          print("Canceled.")

        # INVALID WIN/LOSS SELECTION
        case _:
          print("Invalid selection.")
        
      # REWARD & RESET PROGRESS WHEN >= 30
      if data["comp_progress"] >= 30:
        data["comp_progress"] -= 30
        data["comp_points"] += 100

    case "V":
      print("View Stats")
      stats_choice = input("[G] Caclulate remaining games\n").upper()
      match stats_choice:

        # CALCULATE REMAINING GAMES
        case "G":
          calculate_games_left(int(input("What % is your winrate?\n")))
          # TODO ADD CHECKS FOR THIS TOO

    case "U":
      print("Manually Update Stats")
      data = new_data()
      # update_choice = input("[P] Update Competitive Point Count\n[G] Update Competitive Progress Count\n[X] Cancel\n").upper()
      # match update_choice:
      #   case "P":
      #     data["comp_points"] = int(input("How many Competitive Points do you have?\n"))
      #   case "G":
      #     data["comp_progress"] = int(input("How much Competitive Progress / 30 do you have?\n"))
      #   case "X":
      #     print("Canceled.")
      #   case _:
      #     print("Invalid selection.")

    case "X":
      print("Exit Program")
      running = False

    case _:
      print("Invalid selection.")

  if data["comp_points"] >= 3000:
    input("Congrats, you now have enough Competitive Points to Purchase your weapon skin! Please make your purchase and then press [ENTER]")
    data["comp_points"] -= 3000

  save()

  # TODO create fallback if non-numbers are entered, or other invalid selections
  # TODO ADD SCREEN CLEARING