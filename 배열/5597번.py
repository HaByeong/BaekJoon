arr = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    arr[n - 1] = 0

for i in range(30):
    if arr[i] != 0:
        print(arr[i])
