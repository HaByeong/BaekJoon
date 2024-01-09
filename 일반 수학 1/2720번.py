#나의 풀이
n = int(input())
Cent = [25, 10, 5, 1]

for _ in range(n):
    money = int(input())
    arr = []
    for i in range(len(Cent)):
        arr.append(money // Cent[i])
        money %= Cent[i]
    for elem in arr:
        print(elem, end = " ")
    print()

#정석 풀이
T = int(input())
Cent = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())

    Num = [0] * 4
    for index, val in enumerate(Cent):
        Num[index] = C // val
        C %= val
    print(*Num)