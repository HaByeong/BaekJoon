#정석 풀이
n = int(input())
gen = 0

for i in range(1, n):
    digits = [int(j) for j in str(i)]
    if sum(digits) + i == n:
        gen = i
        trigger = False
        break
print(gen)