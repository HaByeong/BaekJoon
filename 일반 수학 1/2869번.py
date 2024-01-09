import math

#나의 풀이 -> 이러면 안된다.
A, B, V = map(int, input().split())

snailUp = 0


for day in range(1, V):
    snailUp += A
    if snailUp >= V:
        print(day)
        break
    snailUp -= B

#정석 풀이 -> 식을 이용하자
A, B, V = map(int, input().split())

day = (V - A) / (A - B)
print(math.ceil(day) + 1)