import functools
file = open('input.in', 'r')
lanternfish_line = file.readline()
lanternfishes = [int(fish.strip()) for fish in lanternfish_line.split(',')]
print(lanternfishes)


def get_next_day(day):
    i = 0
    new_fishes = day[0]
    next_day = day.copy()
    while i < len(day):
        if i != 6 and i != 8:
            next_day[i] = day[i + 1]
        elif i == 6:
            next_day[i] = day[i + 1] + new_fishes
        elif i == 8:
            next_day[i] = new_fishes
        i += 1
    return next_day

first_day_state = [0] * 9
for fish in lanternfishes:
    first_day_state[fish] += 1
print(first_day_state)

# defi1 = 80 days, defi 2 = 256 days
state = first_day_state.copy()
for i in range(256):
    state = get_next_day(state)

fish_sum = functools.reduce(lambda a, b: a+b, state)

print(fish_sum)
# [0,   1,  2,  3,  4,  5, 6, 7, 8]
# [3, 144, 39, 45, 34, 38, 5, 2, 1]




