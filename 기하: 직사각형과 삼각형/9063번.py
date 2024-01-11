#나의 풀이
x = []
y = []
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

left = max(y) - min(y)
right = max(x) - min(x)

print(left * right)