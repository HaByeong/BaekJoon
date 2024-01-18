import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
arr = list(map(int, input().split()))
newArr = list(set(arr))
newArr.sort()

dic = {}

for i in range(len(newArr)):
    dic[newArr[i]] = i

for num in arr:
    print(dic[num], end = " ")



