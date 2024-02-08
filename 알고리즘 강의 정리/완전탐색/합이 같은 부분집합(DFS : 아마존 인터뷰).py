#합이 같은 부분집합(DFS : 아마존 인터뷰)
import sys
#나의 풀이
def DFS(x):
    if x >= N:
        sumList.append(sum(visit))
        for i in visit:
            print(i, end = " ")
        print()
        return
    else:
        visit.append(numList[x])
        DFS(x + 1)
        visit.pop()
        DFS(x + 1)


N = int(input())
numList = list(map(int, input().split()))
visit = []
sumList = []

DFS(0)
num = 0
for i in sumList:
    cnt = 0
    num = sumList.count(i)
    if num >= 2:
        break

if num >= 2:
    print("YES")
else:
    print("NO")

#정석 풀이
def DFS(L, sum):
    if L == n:
        if sum == (total - sum):
            print("YES")
            #프로그램 강제 종료!!!
            sys.exit(0)
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)
DFS(0, 0)