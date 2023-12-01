with open("input.txt", "r") as file:
    lines = file.read().splitlines()

value = 0
for line in lines:
    line = list(line)
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    if len(nums) == 1:
        value += nums[0]*11
    elif len(nums) > 1:
        value += nums[0]*10+nums[-1]
print(value)
