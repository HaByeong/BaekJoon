#이진트리순회(DFS)
import sys
input = lambda : sys.stdin.readline().rstrip()
#7까지의 노드로 이진 트리 그려본다면

#전위 순회
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end = " ")
        DFS(v * 2)
        DFS(v * 2 + 1)

#중위 순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        print(v, end = " ")
        DFS(v * 2 + 1)

#후위 순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        DFS(v * 2 + 1)
        print(v, end = " ")