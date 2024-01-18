import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
arr_2d = [
    list(input().split())
    for _ in range(N)
]

for i in range(N):
    arr_2d[i].append(i)

arr_2d.sort(key = lambda x : (int(x[0]), x[2]))

for i in range(N):
    print(arr_2d[i][0], arr_2d[i][1])

#정석 풀이
N = int(input())
arr = []

for i in range(N):
    n, m = input().split()
    arr.append([n, m, i])

arr.sort(key = lambda x : (int(x[0]), x[2]))

for i in range(N):
    print(arr[i][0], arr[i][1])