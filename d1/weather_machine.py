input = open("data/weather_machine.txt", "r")

instructions = input.read()

level = 0
index = 0
for i in instructions:
    index += 1
    if (i == '('):
      level += 1
    elif (i == ')'):
      level -= 1
      
    if (level < 0):
      break
    
print(index)