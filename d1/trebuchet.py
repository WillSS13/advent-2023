# calibration = open("data/example1.txt", "r")
# calibration = open("data/example2.txt", "r")
calibration = open("data/trebuchet.txt", "r")

lines = calibration.readlines()

# ======= Part 1 =======
sum = 0
for line in lines:
  
  size = 0
  digits = ""
  for char in line:
    
    if char.isdigit():
      digits += char
      size+=1
          
  code = int(digits[0]) * 10 + int(digits[size-1])
  sum += code
  
print(sum)

# ======= Part 2 =======
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in lines:
  size = 0
  digits = ""

  curr = ""
  for char in line:
    curr += char
    
    if char.isdigit():
      digits += char
      size+=1

    for i in range(len(nums)):
      if (nums[i] in curr):
        digits += str(i+1)
        size += 1
        curr = curr[-1]
          
  code = int(digits[0]) * 10 + int(digits[size-1])
  sum += code
    
print(sum)