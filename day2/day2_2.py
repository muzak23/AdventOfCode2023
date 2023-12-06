with open("input.txt", "r") as file:
    lines = file.read().splitlines()


final_count = 0
for line in lines:
    game = line.split(":")
    draws = game[1].split(";")
    max_red = 0
    max_green = 0
    max_blue = 0
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
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue
    final_count += max_red * max_green * max_blue

print(final_count)
