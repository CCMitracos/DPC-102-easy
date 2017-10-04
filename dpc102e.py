# DPC 102 [E]
# Dice Roller

x = raw_input("string >> ")

if (x[0] == "d"):
    a = int(1)
    b = int(x[1])
    if (len(x) == 2):
        c = int(0)
    else:
        if (x[2] == "+"):
            c = int(x[3])
        else:
            c = -int(x[3])
else:
    a = int(x[0])
    b = int(x[2])
    if (len(x) == 3):
        c = int(0)
    else:
        if (x[3] == "+"):
            c = int(x[4])
        else:
            c = -int(x[4])

print a, b, c
