with open("input.txt", "r") as file:
    lines = file.read().splitlines()

max_red = 12
max_green = 13
max_blue = 14

final_count = 0
for line in lines:
    game = line.split(":")
    draws = game[1].split(";")
    fail = False
    for i in range(len(draws)):
        red = 0
        green = 0
        blue = 0
        picks = draws[i].split(",")
        for j in range(len(picks)):
            color = picks[j].split()[1]
            num = int(picks[j].split()[0])
            if color == "red":
                red += num
            elif color == "green":
                green += num
            elif color == "blue":
                blue += num
        if red > max_red:
            fail = True
        if green > max_green:
            fail = True
        if blue > max_blue:
            fail = True
    if not fail:
        final_count += int(game[0].split(" ")[1])

print(final_count)
