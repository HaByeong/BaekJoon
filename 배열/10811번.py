N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr[i - 1: j] = arr[i - 1: j][::-1]
#역순으로 만들어줄 때 arr[][::-1]을 이용하면 된다
for elem in arr:
    print(elem, end = " ")