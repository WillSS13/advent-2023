
# input = open("data/example.txt", "r")
input = open("data/cube.txt", "r")

lines = input.readlines()

# ====== Part 1 ======
totals = [["red", "green", "blue"],[12, 13, 14]]
sum = 0
for line in lines:
  game = line.split(":")[0]
  sets = line.split(":")[1].split(";")
  possible = 1
  
  for set in sets:
    grabs = set.split(",")
    
    for grab in grabs:      
      if (possible):
        for i in range(3):
          if (totals[0][i] in grab):
            if (int(grab.split(" ")[1]) > totals[1][i]):
              possible = 0
            
  if (possible):
    sum += int(game.split(" ")[1])
    
print(sum)

# ====== Part 2 ======
sum = 0
for line in lines:
  game = line.split(":")[0]
  grabs = line.split(":")[1]

  delimiters = [",", ";"]
  
  for delimiter in delimiters:
    grabs = " ".join(grabs.split(delimiter))
 
  result = grabs.split()
  
  maximums = [["red", "green", "blue"],[1, 1, 1]]
    
  for i in range(int(len(result)/2)):
    for j in range(3):
      if (result[i*2+1] in maximums[0][j]):
        if (int(result[i*2]) > int(maximums[1][j])):
          maximums[1][j] = result[i*2]
  
  product = 1      
  for max in maximums[1]:
    product *= int(max)
    
  sum += product
  
print(sum)