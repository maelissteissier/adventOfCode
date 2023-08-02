with open('entry') as file:
    entry = file.read()
    print(entry)

coords_santa = (0,0)

coords = (0,0)
houses_visited = {(0,0)}

for idx, dir in enumerate(entry):

    if dir == '^':
        if idx % 2 == 0:
            new_coords_santa = (coords_santa[0] + 1, coords_santa[1])
        else:
            new_coords = (coords[0]+1, coords[1])
    elif dir == 'v':
        if idx % 2 == 0:
            new_coords_santa = (coords_santa[0]-1, coords_santa[1])
        else:
            new_coords = (coords[0] - 1, coords[1])
    elif dir == '>':
        if idx % 2 == 0:
            new_coords_santa = (coords_santa[0], coords_santa[1]+1)
        else:
            new_coords = (coords[0], coords[1] + 1)
    else:
        if idx % 2 == 0:
            new_coords_santa = (coords_santa[0], coords_santa[1]-1)
        else:
            new_coords = (coords[0], coords[1] - 1)
    if idx % 2 == 0:
        houses_visited.add(new_coords_santa)
        coords_santa = new_coords_santa
    else:
        houses_visited.add(new_coords)
        coords = new_coords
print(len(houses_visited))
