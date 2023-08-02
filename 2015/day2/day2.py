with open('entry') as file:
    entry = file.read()
    print(entry)

gifts = [gift.split("x") for gift in entry.split("\n")]

total_gift_wrap = 0
for gift in gifts:
    l = int(gift[0])
    w = int(gift[1])
    h = int(gift[2])
    giftwrap = 2 * l * w + 2 * w * h + 2 * h * l
    sorted = [l,w,h]
    sorted.sort()
    mins = sorted[0:2]
    extra = mins[0] * mins[1]
    total_gift_wrap = total_gift_wrap + giftwrap + extra

print(total_gift_wrap)