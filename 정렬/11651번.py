import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

arr_2d.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(arr_2d[i][0], arr_2d[i][1])

#정석 풀이
#나의 풀이가 곧 정석!!