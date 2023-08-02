file = open('input.in', 'r')
inputs = file.readlines()
inputs_clean = [line.strip() for line in inputs]
print(inputs_clean)

entries = [input.split(' ') for input in inputs_clean]

dict_entries = []
is_signal = True
for digits_line in entries:
    new_entry = {'signal': [], 'output': []}
    for digits in digits_line:
        if digits == '|':
            is_signal = False
        elif is_signal:
            new_entry['signal'].append(set([char for char in digits]))
        else:
            new_entry['output'].append(set([char for char in digits]))
    dict_entries.append(new_entry)
    is_signal = True

print(dict_entries)


def count_1_3_7_8(dict_entry):
    count = 0
    for entry in dict_entry:
        for output in entry['output']:
            if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
                count += 1
    return count


print(count_1_3_7_8(dict_entries))

# 0 : 6
# 1 : 2 UNIQ
# 2 : 5
# 3 : 5
# 4 : 4 UNIQ
# 5 : 5
# 6 : 6
# 7 : 3 UNIQ
# 8 : 7 UNIQ
# 9 : 6
#
# 2:1
# 3:7
# 4:4
# 5:2,3,5
# 6:0,6,9
# 7:8


#    8    2,3,5 2,3,5 2,3,5  7   0,6,9 0,6,9   4   0,6,9  1
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf


#    8    !2,!3,5 2,!3,!5 !2,3,!5  7  !0,!6,9 !0,6,!9   4   0,!6,!9  1
# abcdefg bcdef   acdfg   abcdf   abd abcdef   bcdefg   abef abcdeg ab |
# bcdef abcdf bcdef abcdf

# d en haut car 7 a le haut mais pas 4 et 7 possede d mais pas 4
# ef gaucheHaut et milieu (sait pas lequel) car 7 n'a pas ceux la mais 4 oui
# b en bas car 6 n'a que b'
# F MILIEU car 2 ou 3 n'ont que f et pas e
# donc e = haut gauche
# POsitions :
# haut milieu bas gaucheHaut. droite haut, gaucheBas, droiteBas
#
#  dddd
# e    a
# e    a
#  ffff
#      b
#      b

# pos = ['N', 'NW', 'NE', 'MID', 'S', 'SW', 'SE']
# N = ''
# NW = ''
# NE = ''
# MID = ''
# S = ''
# SW = ''
# SE = ''
#
# numbers_dict = {0: [N, NW, NE, SW, SE, S],
#                 1: [NE, SE],
#                 2: [N, NE, MID, SW, S],
#                 3: [N, NE, MID, SE, S],
#                 4: [NW, NE, MID, SE],
#                 5: [N, NW, MID, SE, S],
#                 6: [N, NW, MID, SW, SE, S],
#                 7: [N, NE, SE],
#                 8: [N, NW, NE, MID, SW, SE, S],
#                 9: [N, NW, NE, MID, SE, S]}


# DEFi 2
def verify_possibility(dict_single_entry, possibility):
    N = 0
    NW = 1
    NE = 2
    MID = 3
    SW = 4
    SE = 5
    S = 6
    numbers_dict = {0: {possibility[N], possibility[NW], possibility[NE], possibility[SW], possibility[SE], possibility[S]},
                    1: {possibility[NE], possibility[SE]},
                    2: {possibility[N], possibility[NE], possibility[MID], possibility[SW], possibility[S]},
                    3: {possibility[N], possibility[NE], possibility[MID], possibility[SE], possibility[S]},
                    4: {possibility[NW], possibility[NE], possibility[MID], possibility[SE]},
                    5: {possibility[N], possibility[NW], possibility[MID], possibility[SE], possibility[S]},
                    6: {possibility[N], possibility[NW], possibility[MID], possibility[SW], possibility[SE], possibility[S]},
                    7: {possibility[N], possibility[NE], possibility[SE]},
                    8: {possibility[N], possibility[NW], possibility[NE], possibility[MID], possibility[SW], possibility[SE], possibility[S]},
                    9: {possibility[N], possibility[NW], possibility[NE], possibility[MID], possibility[SE], possibility[S]}}
    final_map = {}
    prop_is_valid = True
    for signal in dict_single_entry['signal']:
        # digit 1
        if len(signal) == 2:
            if signal != numbers_dict[1]:
                prop_is_valid = False
            else:
                final_map[1] = signal
        # digit 7
        elif len(signal) == 3:
            if signal != numbers_dict[7]:
                prop_is_valid = False
            else:
                final_map[7] = signal
        # digit 4
        elif len(signal) == 4:
            if signal != numbers_dict[4]:
                prop_is_valid = False
            else:
                final_map[4] = signal
        # digits 2, 3 or 5
        elif len(signal) == 5:
            if signal != numbers_dict[2] and signal != numbers_dict[3] and signal != numbers_dict[5]:
                prop_is_valid = False
            else:
                if signal == numbers_dict[2]:
                    final_map[2] = signal
                elif signal == numbers_dict[3]:
                    final_map[3] = signal
                elif signal == numbers_dict[5]:
                    final_map[5] = signal
        # digits 0, 6 or 9
        elif len(signal) == 6:
            if signal != numbers_dict[0] and signal != numbers_dict[6] and signal != numbers_dict[9]:
                prop_is_valid = False
            else:
                if signal == numbers_dict[0]:
                    final_map[0] = signal
                elif signal == numbers_dict[6]:
                    final_map[6] = signal
                elif signal == numbers_dict[9]:
                    final_map[9] = signal
        # digit 8
        elif len(signal) == 7:
            if signal != numbers_dict[8]:
                prop_is_valid = False
                final_map[7] = signal

    return prop_is_valid, None if not prop_is_valid else decode_output(final_map, dict_single_entry['output']), numbers_dict

def decode_output(right_combination, encoded_output):
    output = 0
    for digit in encoded_output:
        if len(digit) == 2:
            output = output * 10 + 1
        elif len(digit) == 3 :
            output = output * 10 + 7
        elif len(digit) == 4 :
            output = output * 10 + 4
        elif len(digit) == 7:
            output = output * 10 + 8
        elif len(digit) == 5 :
            if digit == right_combination[2]:
                output = output * 10 + 2
            elif digit == right_combination[3]:
                output = output * 10 + 3
            elif digit == right_combination[5]:
                output = output * 10 + 5
        elif len(digit) == 6 :
            if digit == right_combination[0]:
                output = output * 10 + 0
            elif digit == right_combination[6]:
                output = output * 10 + 6
            elif digit == right_combination[9]:
                output = output * 10 + 9
    return output





list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def combine(size, items):
    return combine_inner(size, [], items, [])


def combine_inner(size, prefix, items, combis):
    if len(items) == 0 or len(prefix) == size:
        combis.append(prefix)
        return combis
    else:
        for idx, item in enumerate(items):
            new_prefix = prefix.copy()
            new_prefix.append(item)
            new_items = items.copy()
            del new_items[idx]
            combis = combine_inner(size, new_prefix, new_items, combis)
        return combis



combinations = combine(7, list)
print("Len combination :", str(len(combinations)))

sum_outputs = 0
for entry in dict_entries:
    for combination in combinations:
        valid, output, num_dict = verify_possibility(entry, combination)
        if valid:
            sum_outputs = sum_outputs + output
            break

print(sum_outputs)

# combination = ['d', 'e', 'a', 'f', 'g', 'b', 'c']
#
# valid, output = verify_possibility(dict_entries[0], combination)
#
# print(output)