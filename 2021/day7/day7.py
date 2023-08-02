import functools
import sys
file = open('input.in', 'r')
crabs_line = file.readline()
crabs = [int(fish.strip()) for fish in crabs_line.split(',')]

print(crabs)
crabs.sort()
print(crabs)

# ----- Defi 1 -------

# med_pos = len(crabs)//2
# print(med_pos)
# horizontal_pos = crabs[med_pos]

# uniques = list(dict.fromkeys(crabs))
# print(uniques)

# fuels = list(map(lambda x: abs(x - horizontal_pos), crabs))
# fuel = functools.reduce(lambda a, b: a+b, fuels)

# print(fuels)
# print(fuel)

# ------- Defi 2 -------

# ---- Optimized -----

moy = 0
for crab in crabs:
    moy = moy + crab
moy = moy // len(crabs)
print(moy)

fuels = list(map(lambda x: round(((abs(x - moy) * (abs(x - moy) + 1))/2)), crabs))
fuel = functools.reduce(lambda a, b: a+b, fuels)

print(fuels)
print(fuel)

# 104822130


# ------ BRUTE FORCE -------
# def find_total_fuel(crabs, test_position):
#     total_fuel = 0
#     for crab in crabs:
#         fuel_needed = round(((abs(crab - i) * (abs(crab - i) + 1)) / 2))
#         total_fuel = total_fuel + fuel_needed
#
#     return total_fuel
#
#
# i = crabs[0]
# min_fuel = { 'idx': 0, 'fuel': sys.maxsize}
# while i < crabs[len(crabs) - 1]:
#     possible_fuel = find_total_fuel(crabs, i)
#     if possible_fuel < min_fuel['fuel']:
#         min_fuel = { 'idx': i, 'fuel': possible_fuel}
#
#     i = i + 1
# print(min_fuel)

# 104822130