with open('entry') as file:
    entry = file.read()

strings_listify = [c for c in [line for line in entry.split('\n')]]


def pass_rule_one(santa_str):
    return find_same_pair_rec(set(), santa_str[0]+santa_str[1], santa_str[2:])


# contains a pair of any two letters that appears at least twice in the string without overlapping,
# like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#
# Recursive execution
# ab cdefg
#  bc defg               | ab
#   cd efg | ab          | bc
#    de fg | ab bc       | cd
#     ef g | ab bc cd    | de
#      fg  | ab bc cd de | ef
#
# ab cdefgh
#  bc defgh                  | ab
#   cd efgh | ab             | bc
#    de fgh | ab bc          | cd
#     ef gh | ab bc cd       | de
#      fg h | ab bc cd de    | ef
#       gh  | ab bc cd de ef | fg
def find_same_pair_rec(pair_found_set, pair_jumped, rest):
    new_pair = pair_jumped[1] + rest[0]
    if new_pair in pair_found_set:
        return True
    elif len(rest) == 1:
        return False
    else:
        if pair_jumped is not None:
            pair_found_set.add(pair_jumped)
        return find_same_pair_rec(pair_found_set, new_pair, rest[1:])


def pass_rule_two(santa_str_listified):
    pass_rule = False
    i = 0
    while i < len(santa_str_listified) - 2 and not pass_rule:
        pass_rule = santa_str_listified[i] == santa_str_listified[i+2]
        i = i + 1
    return pass_rule


nice_strings = 0
for santa_str in strings_listify:
    if pass_rule_one(santa_str) and pass_rule_two(santa_str):
        nice_strings = nice_strings + 1


print(nice_strings)



