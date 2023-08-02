file = open('input.in', 'r')
lines_newline = file.readlines()
lines = [line.strip() for line in lines_newline]

matrix = [[int(char) for char in line] for line in lines]


def bin_to_decimal(bit_list_little_endian):
    i = len(bit_list_little_endian) - 1
    power = 0
    decimal = 0
    while i >= 0:
        decimal = decimal + (bit_list_little_endian[i] * pow(2, power))
        power += 1
        i -= 1
    return decimal

def bitwise_not(bit_list_little_endian):
    not_bits = []
    for i in range(len(bit_list_little_endian)):
        not_bits.append(0 if bit_list_little_endian[i] == 1 else 1)
    return not_bits

# DEFI 1
middle = len(lines)/2
# of course, if matrix size > 0
gamma_size = len(matrix[0])
oxygen_bits = []
i = 0
for i in range(gamma_size):
    sum_bin = 0
    for j in range(len(lines)):
        sum_bin += matrix[j][i]
    oxygen_bits.append(1 if sum_bin > middle else 0)

epsilon_bits = bitwise_not(oxygen_bits)

gamma_decimal = bin_to_decimal(oxygen_bits)
epsilon_decimal = bin_to_decimal(epsilon_bits)


# print(matrix)
# print(oxygen_bits)
# print(epsilon_decimal)
# print(gamma_decimal)
# print(epsilon_decimal * gamma_decimal)

# DEFI 2

middle = len(lines)/2
# of course, if matrix size > 0
oxygen_size = len(matrix[0])
oxygen_bits = []
oxygen_matrix = matrix
keepers = []

for i in range(oxygen_size):
    sum_bin = 0
    keepers = []
    for j in range(len(oxygen_matrix)):
        sum_bin += oxygen_matrix[j][i]
    # oxygen_bits.append(1 if sum_bin >= middle else 0)
    bit = 1 if sum_bin >= middle else 0
    for k in range(len(oxygen_matrix)):
        if oxygen_matrix[k][i] == bit:
            keepers.append(oxygen_matrix[k])
    oxygen_matrix = keepers
    middle = len(oxygen_matrix) / 2
    if len(keepers) == 1:
        break

co2_bits = []
co2_matrix = matrix
keepers = []
middle = len(lines)/2
for i in range(oxygen_size):
    sum_bin = 0
    keepers = []
    for j in range(len(co2_matrix)):
        sum_bin += co2_matrix[j][i]
    # oxygen_bits.append(1 if sum_bin >= middle else 0)
    bit = 1 if sum_bin < middle else 0
    for k in range(len(co2_matrix)):
        if co2_matrix[k][i] == bit:
            keepers.append(co2_matrix[k])
    co2_matrix = keepers
    middle = len(co2_matrix) / 2
    if len(keepers) == 1:
        break

    #[[0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]]

# oxygen_matrix = matrix
#
# for i in range(oxygen_size):
#     keepers = []
#     for j in range(len(oxygen_matrix)):
#         if matrix[j][i] == oxygen_bits[i]:
#             keepers.append(matrix[j])
#     oxygen_matrix = keepers if len(keepers) > 0 else oxygen_matrix
#
# co2_bits = bitwise_not(oxygen_bits)
#
# co2_matrix = matrix
# for i in range(oxygen_size):
#     keepers = []
#     for j in range(len(co2_matrix)):
#         if matrix[j][i] == co2_bits[i]:
#             keepers.append(matrix[j])
#     co2_matrix = keepers if len(keepers) > 0 else co2_matrix

print(oxygen_bits)
print(oxygen_matrix)
print(co2_matrix)
oxygen_decimal = bin_to_decimal(oxygen_matrix[0])
co2_decimal = bin_to_decimal(co2_matrix[0])
print(oxygen_decimal * co2_decimal)
# print(co2_bits)
# print(co2_matrix)