with open('entry') as file:
    entry = file.read()
    print(entry)

coords = (0,0)
houses_visited = {(0,0)}
for dir in entry:
    if dir == '^':
        new_coords = (coords[0]+1 , coords[1])
    elif dir == 'v':
        new_coords = (coords[0]-1, coords[1])
    elif dir == '>':
        new_coords = (coords[0], coords[1]+1)
    else:
        new_coords = (coords[0], coords[1]-1)
    houses_visited.add(new_coords)
    coords = new_coords

print(len(houses_visited))
