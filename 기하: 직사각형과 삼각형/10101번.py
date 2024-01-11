#나의 풀이
arr = []
cnt = 0
sum_val = 0

for _ in range(3):
    n = int(input())
    if n in arr:
        arr.append(n)
        cnt += 1
        sum_val += n
    else:
        arr.append(n)
        sum_val += n
if cnt == 2 and sum_val == 180:
    print("Equilateral")
elif cnt == 1 and sum_val == 180:
    print("Isosceles")
elif cnt == 0 and sum_val == 180:
    print("Scalene")
else:
    print("Error")


