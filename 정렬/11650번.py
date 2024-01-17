import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

arr_2d.sort()
for row in arr_2d:
    for elem in row:
        print(elem, end = " ")
    print()

#정석 풀이!! sort(key = lambda x : (x[0], x[1])) 이용

N = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

arr_2d.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(arr_2d[i][0], arr_2d[i][1])