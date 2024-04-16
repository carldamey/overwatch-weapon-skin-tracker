import csv, math, os, pandas, random
data = {}
running = True

def cls():
  # WINDOWS
  if os.name == "nt":
    os.system("cls")
  # LINUX / OSX
  else:
    os.system("clear")

def save(data):
  dataframe = pandas.DataFrame({
    "comp_points": [int(data["comp_points"])],
    "comp_progress": [int(data["comp_progress"])],
  })
  dataframe.to_csv("data.csv", index=False)

def new_data():
  input_data = {
    "comp_points": "",
    "comp_progress": "",
  }
  while not input_data["comp_points"].isdigit():
    cls()
    input_data["comp_points"] = input("How many competitive points do you have?\n")
  while not input_data["comp_progress"].isdigit():
    cls()
    input_data["comp_progress"] = input("What is your current competitive progress / 30?\n")
    cls()
  return input_data

def load():
  if not os.path.exists("data.csv"):
    print("No data found, creating data file.\n")
    data = new_data()
    save(data)
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
  cls()
  data = load()
  # COMP POINT COUNT MET
  while data["comp_points"] >= 3000:
    input(f"Congrats, you have {data['comp_points']} Competitive Points, enough to Purchase your weapon skin! Please make your purchase and then press [ENTER]")
    data["comp_points"] -= 3000

  print(f"You have {data['comp_points']} Points and {data['comp_progress']} / 30 Progress.")
  primary_choice = input("What would you like to do?\n[A] Add Game\n[V] View Stats\n[U] Update Stats Manually\n[X] Exit Program\n").upper()
  match primary_choice:

    # ADD GAME RESULT
    case "A":
      cls()
      print("Add Game")
      win_loss_choice = input("[W] Win\n[L] Loss\n[X] Cancel\n").upper()
      match win_loss_choice:

        # GAME WON
        case "W":
          cls()
          data["comp_points"] += 10
          data["comp_progress"] += 3
          input("Win logged!")

        # GAME LOST
        case "L":
          cls()
          data["comp_progress"] += 1
          input("Loss logged.")

        # CANCELED
        case "X":
          cls()
          input("Canceled.")

        # INVALID WIN/LOSS SELECTION
        case _:
          cls()
          input("Invalid selection.")
        
      # REWARD & RESET PROGRESS WHEN >= 30
      if data["comp_progress"] >= 30:
        data["comp_progress"] -= 30
        data["comp_points"] += 100

    # VIEW STATS
    case "V":
      cls()
      print("View Stats")
      stats_choice = input("[G] Caclulate remaining games\n[X] Cancel\n").upper()
      cls()
      match stats_choice:

        # CALCULATE REMAINING GAMES
        case "G":
          cls()
          winrate = ""
          while not winrate.isdigit():
            winrate = input("What % is your winrate?\n")
          calculate_games_left(int(winrate))

        # CANCEL
        case "X":
          cls()
          input("Canceled")

        # INVALID SELECTION
        case _:
          cls()
          input("Invalid Selection")

    # UPDATE STATS
    case "U":
      cls()
      print("Manually Update Stats")
      data = new_data()

    # EXIT PROGRAM
    case "X":
      cls()
      print("Goodbye.")
      running = False

    # INVALID SELECTION
    case _:
      cls()



  save(data)

  # TODO ADD SCREEN CLEARING
  # TODO ADD RELATIVE DATA PATHING