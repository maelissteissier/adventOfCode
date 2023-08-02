with open('entry') as file:
    entry = file.read()
    print(entry)

up = entry.replace(')', "")
down = entry.replace('(', "")

floor = len(up) - len(down)
print(floor)
