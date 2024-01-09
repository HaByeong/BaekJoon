#나의 풀이
N, k = map(int, input().split())

cnt = 0

for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
if cnt < k:
    print(0)

#정석 풀이
N, k = map(int, input().split())

result = 0

for i in range(1, N + 1):
    if N % i == 0:
        k -= 1
    if k == 0:
        result = i
        break
print(result)