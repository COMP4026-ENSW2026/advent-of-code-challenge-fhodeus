f = open("01-advent-of-code-challenge/01/sample.in", "r")
f_striped = f.read().strip()

calories_array = [i for i in f_striped.split('\n')]

# Armazena a maior caloria
higher_calorie = 0
# Armazena a caloria atual do loop
current_calorie = 0

# loop
for calories in calories_array:
  if calories == '':
    if current_calorie > higher_calorie:
      higher_calorie = current_calorie
    current_calorie = 0
  else:
    current_calorie += int(calories)

print(higher_calorie)