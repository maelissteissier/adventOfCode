file = open('input.in', 'r')
lines_newline = file.readlines()
lines = [line.strip() for line in lines_newline]
commands = [ {"command": line.split(' ')[0], "val": int(line.split(' ')[1])} for line in lines]

# of course we should check the type of the entries at this point but I trust advent of code
print(commands)

# DEFI 1
# horiz = 0
# depth = 0
#
# for command in commands:
#     if command["command"] == "forward":
#         horiz += command["val"]
#     elif command["command"] == "down":
#         depth += command["val"]
#     elif command["command"] == "up":
#         depth -= command["val"]
#
# print(horiz * depth)

# Defi 2

horiz = 0
depth = 0
aim = 0

for command in commands:
    if command["command"] == "forward":
        horiz += command["val"]
        depth += aim * command["val"]
    elif command["command"] == "down":
        aim += command["val"]
    elif command["command"] == "up":
        aim -= command["val"]

print(horiz * depth)
