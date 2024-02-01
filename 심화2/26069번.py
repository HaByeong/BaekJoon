import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
rainBow = set()


for _ in range(N):
    A, B = input().split()
    if A == "ChongChong" or B == "ChongChong":
        rainBow.add(A)
        rainBow.add(B)
    if A in rainBow or B in rainBow:
        rainBow.add(A)
        rainBow.add(B)
print(len(rainBow))

#정석 풀이
N = int(input())
rainBow = set()
rainBow.add("ChongChong")

for _ in range(N):
    A, B = input().split()
    if A in rainBow or B in rainBow:
        rainBow.add(A)
        rainBow.add(B)

print(len(rainBow))
