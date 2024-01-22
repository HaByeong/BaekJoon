import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
A, B = map(int, input().split())

setA = set(input().split())
setB = set(input().split())

setA_B = setA - setB
setB_A = setB - setA

setAB = setA_B | setB_A

print(len(setAB))

#정석 풀이
A, B = map(int, input().split())

setA = set(input().split())
setB = set(input().split())

setAB = (setA - setB) | (setB - setA)
print(len(setAB))

#아니면 setAB를 구하지 말고
print(len(setA - setB) + len(setB - setA))