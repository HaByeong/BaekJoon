import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 index가 0이면 output이 numList[0]이 아니라 계산된 이후의 output
def DFS(index, output):
    if index == (N - 1):
        ans.append(output)
        return
    for i in range(4):
        if cntList[i] == funList[i]:
            continue
        cntList[i] += 1
        if i == 0:
            DFS(index + 1, output + numList[index + 1])
        elif i == 1:
            DFS(index + 1, output - numList[index + 1])
        elif i == 2:
            DFS(index + 1, output * numList[index + 1])
        else:
            if output < 0:
                DFS(index + 1, (output * -1 // numList[index + 1]) * -1)
            else:
                DFS(index + 1, output // numList[index + 1])
        cntList[i] -= 1

N = int(input())
numList = list(map(int, input().split()))
funList = list(map(int, input().split()))
ans = []
cntList = [0] * 4
DFS(0, numList[0])

print(max(ans))
print(min(ans))