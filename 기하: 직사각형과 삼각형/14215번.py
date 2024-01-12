#나의 풀이
arr = list(map(int, input().split()))
max_val = max(arr)
arr.remove(max_val)
if sum(arr) <= max_val:
    max_val = sum(arr) - 1
    print(max_val + sum(arr))
else:
    print(max_val + sum(arr))

#정석 풀이

a, b ,c = sorted(map(int, input().split()))
c = min(c, a + b - 1)
print(a + b + c)