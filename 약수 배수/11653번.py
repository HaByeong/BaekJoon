#나의 풀이
n = int(input())
i = 2

while n != 1:
    if n % i == 0:
       print(i)
       n //= i
    else:
        i += 1
#정석 풀이
#나의 풀이가 정석