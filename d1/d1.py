# calibration = open("data/example1.txt", "r")
# calibration = open("data/example2.txt", "r")
calibration = open("data/input.txt", "r")

lines = calibration.readlines()

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
for line in lines:
  idx = 0
  curr = ""
  
  size = 0
  digits = ""
  for char in line:
    idx += 1
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