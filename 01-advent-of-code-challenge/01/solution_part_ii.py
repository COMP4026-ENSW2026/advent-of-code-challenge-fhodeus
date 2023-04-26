f = open("01-advent-of-code-challenge/01/sample.in", "r")
f_striped = f.read().strip()

calories_array = [i for i in f_striped.split('\n')]

# Armazena a maior caloria
higher_calorie = []
# Armazena a caloria atual do loop
current_calorie = 0

# loop
for calories in calories_array:
    if calories == '':
        higher_calorie.append(current_calorie)
        current_calorie = 0
    else:
        current_calorie += int(calories)

sum_higher_calorie = 0
for i in range(3):
    sum_higher_calorie += max(higher_calorie)
    higher_calorie.remove(max(higher_calorie))
    
print(sum_higher_calorie)