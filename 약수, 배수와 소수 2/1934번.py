import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A,B))
#정석 풀이 -> 동일하게 math 라이브러리를 이용하자