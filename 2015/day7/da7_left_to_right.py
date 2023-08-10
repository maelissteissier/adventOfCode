# 0000 0000 0111 1011
# 0000 0001 1100 1000

# 0000 0000 0100 1000

# AND &
# OR |
# NOT ~
# LSHIFT <<
# RSHIFT >>


def digest_instr(instr, state_set):
    try:
        num = int(instr[0])
        if instr[1] == "AND":
            left_exp = num
            right_exp = eval_exp(state_set, instr[2])
            if right_exp is None:
                state_set = store_action(state_set, instr, instr[2])
            else:
                dest = instr[4]
                state_set = save_value(state_set, dest, apply_left_right_operation(left_exp, right_exp, "AND"))
                # trigger digest of state_set dest actions now that it has a value
                resolve_actions(state_set[dest]["actions"], state_set)
        else:
            dest = instr[2]
            state_set = save_value(state_set, dest, num)
            # trigger digest of state_set dest actions now that it has a value
            resolve_actions(state_set[dest]["actions"], state_set)
    except ValueError:
        num = None

    if num is None:
        if instr[0] == "NOT":
            exp = eval_exp(state_set, instr[1])
            if exp is None:
                state_set = store_action(state_set, instr, instr[1])
            else:
                dest = instr[3]

                state_set = save_value(state_set, dest, ~exp)
                # trigger digest of state_set dest actions now that it has a value
                resolve_actions(state_set[dest]["actions"], state_set)
        elif instr[1] == "->":
            exp = eval_exp(state_set, instr[0])
            if exp is None:
                state_set = store_action(state_set, instr, instr[0])
            else:
                dest = instr[2]
                state_set = save_value(state_set, dest, exp)
                # trigger digest of state_set dest actions now that it has a value
                resolve_actions(state_set[dest]["actions"], state_set)
        else:
            left_exp = eval_exp(state_set, instr[0])
            if left_exp is None:
                state_set = store_action(state_set, instr, instr[0])
            else:
                operator = instr[1]
                right_exp = int(instr[2]) if (operator == "LSHIFT" or operator == "RSHIFT") else eval_exp(state_set, instr[2])
                if right_exp is None:
                    state_set = store_action(state_set, instr, instr[2])
                else:
                    dest = instr[4]
                    state_set = save_value(state_set, dest, apply_left_right_operation(left_exp, right_exp, operator))
                    # trigger digest of state_set dest actions now that it has a value
                    resolve_actions(state_set[dest]["actions"], state_set)
    return state_set


def eval_exp(state_set, variable):
    if variable in state_set:
        return state_set[variable]['val']
    else:
        return None


def store_action(state_set, action, variable):
    if variable in state_set:
        state_set[variable]["actions"].append(action)
    else:
        state_set[variable] = {"val": None,
                               "actions": [action]}
    return state_set


def apply_left_right_operation(left_exp, right_exp, operator):
    if operator == "AND":
        return left_exp & right_exp
    elif operator == "OR":
        return left_exp | right_exp
    elif operator == "LSHIFT":
        return left_exp << int(right_exp)
    elif operator == "RSHIFT":
        return left_exp >> int(right_exp)


def save_value(state_set, dest, value):
    if dest in state_set:
        state_set[dest]["val"] = value
    else:
        state_set[dest] = {"val": value, "actions": []}
    return state_set

def resolve_actions(actions, state_set):
    actions_cpy = actions.copy()
    for action in actions_cpy:
        actions.pop(0)
        state_set = digest_instr(action, state_set)


def pretty_print_values(state_set):
    for wire in state_set:
        print(wire + ": " + ("None" if state_set[wire]["val"] is None else str(state_set[wire]["val"] & 0xffff)))


# MAIN
with open('entry') as file:
    entry = file.read()
    lines = entry.split("\n")
    tokens = [toks.split(" ") for toks in lines]

state_set = {}

resolve_actions(tokens, state_set)



print(state_set)
pretty_print_values(state_set)