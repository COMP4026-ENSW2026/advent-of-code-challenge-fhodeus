f = open("01-advent-of-code-challenge/01/sample.in", "r")
f_striped = f.read().strip()

calories_array = [i for i in f_striped.split('\n')]

# Armazena a maior caloria
higher_calorie = 0
# Armazena a caloria atual do loop
current_calorie = 0

# loop
for line in calories_array:
    if line:
        current_calorie = current_calorie + int(line)
        pass
    elif current_calorie > higher_calorie:
        higher_calorie = current_calorie
        current_calorie = 0

print(higher_calorie)