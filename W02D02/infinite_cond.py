# continue
a = 1
while a<11:
    if a == 3 or a == 5:
        print(a)
        continue
    print(a, "Odd" if a%2 else "Even")
    a += 1