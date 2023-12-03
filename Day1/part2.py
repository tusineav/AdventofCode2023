file = open("temp.txt")
lines = file.readlines()


def grab_first_digit(str):
    for i in range(0, len(str)):
        if '0' <= str[i] <= '9':
            return str[i]

def fix_nums(string):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(string)):
        if '1' <= string[i] <= '9':
            return string
        for index, num in enumerate(nums):
            if string[i: i + len(num)] == num:
                string = string[0:i] + str(index + 1) + string[i + len(num):]
                return string
                
    return string

def fix_nums_backwards(string):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in reversed(range(0, len(string))):
        if 'i' <= string[i] <= '9':
            return string
        for index, num in enumerate(nums):
            if string[i: i + len(num)] == num:
                string = string[0:i] + str(index + 1) + string[i + len(num):]
                return string
                
    return string
    
    
   
sum = 0
for line in lines:
    line = fix_nums(line)
    line = fix_nums_backwards(line)
    sum += int(str(grab_first_digit(line)) + str(grab_first_digit(line[::-1])))

print(sum)
        
