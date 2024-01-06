n = int(input())

a = n
for i in range(1, n + 1):
    starNum = (2 * i) - 1
    for _ in range(1, a + 1 - starNum):
        print(" ", end = "")
    for _ in range(a + 1 - starNum, a + 1):
        print("*", end = "")
    print()
    if a == starNum:
        break
    a += 1

for i in range(n - 1, 0, -1):
    starNum = (2 * i) - 1
    a -= 1
    for _ in range(1, a + 1 - starNum):
        print(" ", end = "")
    for _ in range(a + 1 - starNum, a + 1):
        print("*", end = "")
    print()



