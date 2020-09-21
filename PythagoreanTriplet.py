s = 1000
match = False
for a in range(1, 1001):
    for b in range(1, 1001):
        c = s-a-b
        if a**2+b**2 == c**2:
            match = True
            print(a, b, c)
            break
        if match:
            break
