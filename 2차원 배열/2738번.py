#나의 풀이
n, m = map(int, input().split())

arr_2d = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr2_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

"""answer_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]"""

for i in range(n):
    for j in range(m):
        s = arr_2d[i][j] + arr2_2d[i][j]
        print(s, end = " ")
    print()

"""for row in answer_2d:
    for elem in row:
        print(elem, end = " ")
    print()"""