file = open('input.in', 'r')
lines_newline = file.readlines()
lines = [int(line.strip()) for line in lines_newline]

# of course we should check the type of the entries at this point but I trust advent of code
print(lines)

# DEFI 1
last_max = lines[0]
inc_count = 0

for line in lines[1:]:
    if line > last_max:
        inc_count += 1
    last_max = line

print("inc_count = " + str(inc_count))

# DEFI 2

last_max = lines[0] + lines[1] + lines[2]
i = 1
inc_count = 0
while i < len(lines) - 2:
    act_max = lines[i] + lines[i + 1] + lines[i + 2]
    if act_max > last_max:
        inc_count += 1
    last_max = act_max
    i += 1
print("inc_count = " + str(inc_count))