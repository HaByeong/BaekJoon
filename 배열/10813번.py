N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

for elem in arr:
    print(elem, end = " ")