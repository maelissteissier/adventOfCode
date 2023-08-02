with open('entry') as file:
    entry = file.read()
    print(entry)

gifts = [gift.split("x") for gift in entry.split("\n")]

total_ribbon = 0
for gift in gifts:
    l = int(gift[0])
    w = int(gift[1])
    h = int(gift[2])

    sorted = [l,w,h]
    sorted.sort()
    mins = sorted[0:2]
    ribbon = 2*mins[0] + 2*mins[1]
    bow = l*w*h
    total_ribbon = total_ribbon + ribbon + bow

print(total_ribbon)