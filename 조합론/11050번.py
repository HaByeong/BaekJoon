import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> nCm 이거랑 같은 이항 계수는
N, K = map(int, input().split())

print(math.factorial(N) // (math.factorial(K) * math.factorial(N - K)))