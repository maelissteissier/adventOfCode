with open('entry') as file:
    entry = file.read()

strings_listify = [c for c in [line for line in entry.split('\n')]]


def pass_rule_one(santa_str_listified):
    valid_vowels = {'a', 'e', 'i', 'o', 'u'}
    acc_vow = 0
    for letter in santa_str_listified:
        acc_vow = acc_vow + 1 if letter in valid_vowels else acc_vow
    return acc_vow >= 3


def pass_rule_two_and_three(santa_str_listified):
    pass_rule_two = False
    invalid_two_letters = {'ab', 'cd', 'pq', 'xy'}
    pass_rule_three = True
    i = 0
    while i < len(santa_str_listified) - 1 and pass_rule_three:
        pass_rule_two = pass_rule_two or santa_str_listified[i] == santa_str_listified[i+1]
        pass_rule_three = not ((santa_str_listified[i] + santa_str_listified[i+1]) in invalid_two_letters)
        i = i + 1
    return pass_rule_two and pass_rule_three


nice_strings = 0
for santa_str in strings_listify:
    if pass_rule_one(santa_str) and pass_rule_two_and_three(santa_str):
        nice_strings = nice_strings + 1


print(nice_strings)