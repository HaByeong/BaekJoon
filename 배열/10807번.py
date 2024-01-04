n = int(input())

arr = list(map(int, input().split()))
num = int(input())

count = 0

for i in range(n):
    if arr[i] == num:
        count += 1
print(count)

