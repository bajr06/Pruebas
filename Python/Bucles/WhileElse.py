i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

i = 5
while i < 5:
    print(i)
    i += 1
    continue
else:
    print("else:", i)
