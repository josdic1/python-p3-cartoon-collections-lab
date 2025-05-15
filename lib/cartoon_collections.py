
def roll_call_dwarves(list):
  for index, d in enumerate(list):
    print(f"{index + 1}. {d}")

def summon_captain_planet(list):
  output = []
  for item in list:
    output.append(f"{item.capitalize()}!")
  return output

def long_planeteer_calls(words):
  for word in words:
    if len(word) > 4:
      return True
  return False

def find_the_cheese(snack_list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for item in snack_list:
        if item in cheese_list:
            return item
    print(None)