import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

fix_price = price[0]
sum_price = fix_price * distance[0]
for i in range(1, N - 1):
    if fix_price > price[i]:
        fix_price = price[i]
        sum_price += fix_price * distance[i]
    else:
        sum_price += fix_price * distance[i]
print(sum_price)
