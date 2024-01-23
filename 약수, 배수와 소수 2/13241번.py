import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
A, B = map(int, input().split())

print(math.lcm(A,B))