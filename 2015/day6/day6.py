def extract_instr(tokens):
    instr = {}
    if tokens[0] == "toggle":
        instr["action"] = "toggle"
        instr["coords"] = extract_coords(tokens[1:])
    else:
        instr["action"] = tokens[1]
        instr["coords"] = extract_coords(tokens[2:])
    return instr


def extract_coords(tokens_cut):
    coords = {
        "start": {},
        "end": {}
    }
    coords["start"]["x"] = int(tokens_cut[0].split(",")[0])
    coords["start"]["y"] = int(tokens_cut[0].split(",")[1])
    coords["end"]["x"] = int(tokens_cut[2].split(",")[0])
    coords["end"]["y"] = int(tokens_cut[2].split(",")[1])
    return coords


def create_start_grid():
    grid = []
    for i in range(1000):
        line = []
        for x in range(1000):
            line.append(False)
        grid.append(line)
    return grid


def pretty_print(grid):
    for line in grid:
        for elem in line:
            print("O" if elem else "X", end="")
        print("")


def get_new_grid(grid, instr):
    y = instr["coords"]["start"]["y"]

    while y <= instr["coords"]["end"]["y"]:
        x = instr["coords"]["start"]["x"]
        while x <= instr["coords"]["end"]["x"]:
            if instr["action"] == "toggle":
                grid[y][x] = not grid[y][x]
            elif instr["action"] == "off":
                grid[y][x] = False
            else:
                grid[y][x] = True
            x = x + 1
        y = y + 1
    return grid


def count_lights_on(grid):
    count = 0
    for ys in grid:
        for x in ys:
            count = count + 1 if x else count
    return count


# MAIN
with open('entry') as file:
    entry = file.read()
    lines = entry.split("\n")
    tokens = [toks.split(" ") for toks in lines]
    instrs = [extract_instr(toks) for toks in tokens]
    print(instrs)
    # print(tokens)


grid = create_start_grid()
print(len(grid))
for instr in instrs:
    grid = get_new_grid(grid, instr)
print(count_lights_on(grid))
pretty_print(grid)


# x ->
# y
# |
# v

# x,y
#
# 0,0                  999,0
#
#
#
#
#
# 0,999                999,999