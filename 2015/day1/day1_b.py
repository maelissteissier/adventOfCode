with open('entry') as file:
    entry = file.read()
    print(entry)

i = 0
neg = False
for idx, instr in enumerate(entry):
    i = i + 1 if instr == "(" else i - 1
    if i < 0 and neg is False:
        print("First neg floor = ", idx + 1)
        neg = True


