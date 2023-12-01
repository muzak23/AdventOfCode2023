import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

for i in range(len(lines)):
    lines[i] = str(lines[i])
    lines[i] = re.sub(r'(one)', '\\1 1\\1', lines[i])
    lines[i] = re.sub(r'(two)', '\\1 2\\1', lines[i])
    lines[i] = re.sub(r'(three)', '\\1 3\\1', lines[i])
    lines[i] = re.sub(r'(four)', '\\1 4\\1', lines[i])
    lines[i] = re.sub(r'(five)', '\\1 5\\1', lines[i])
    lines[i] = re.sub(r'(six)', '\\1 6\\1', lines[i])
    lines[i] = re.sub(r'(seven)', '\\1 7\\1', lines[i])
    lines[i] = re.sub(r'(eight)', '\\1 8\\1', lines[i])
    lines[i] = re.sub(r'(nine)', '\\1 9\\1', lines[i])
    lines[i] = re.sub(r'(zero)', '\\1 0\\1', lines[i])

value = 0
for line in lines:
    line = list(line)
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    if len(nums) == 1:
        value += int(nums[0]*11)
    elif len(nums) > 1:
        value += int(nums[0])*10+int(nums[-1])

print(value)