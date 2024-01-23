import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
A, B = map(int, input().split())
A2, B2 = map(int, input().split())

upNum = A * B2 + B * A2
downNum = B * B2
numGcd = math.gcd(upNum, downNum)

if numGcd == 1:
    print(upNum, downNum)
else:
    print(int(upNum / numGcd), int(downNum / numGcd))

#정석 풀이 -> 내가 정석