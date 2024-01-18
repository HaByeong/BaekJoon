import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
arr = []

for _ in range(N):
    word = input()
    if word not in arr:
        arr.append(word)

arr.sort()
arr.sort(key = lambda x : len(x))

for word in arr:
    print(word)

#정석 풀이
N = int(input())
arr = []

for _ in range(N):
    arr.append(input())
setArr = set(arr)
arr = list(setArr)

arr.sort()
arr.sort(key = len)

for word in arr:
    print(word)
