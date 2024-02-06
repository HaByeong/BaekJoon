#재귀함수를 이용한 이진수 출력
import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def DFS(x):
    if x == 1:
        return print(x, end = "")
    else:
        n = x % 2
        x //= 2
        DFS(x)
        print(n, end = "")

N = int(input())
DFS(N)

#정석 풀이
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end = "")