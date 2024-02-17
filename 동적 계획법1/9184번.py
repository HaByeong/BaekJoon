import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def w(a, b, c):
    if D1.get((a, b, c)) != None:
        return D1[(a, b, c)]
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        ans = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        D1[(a, b, c)] = ans
        return ans
    else:
        ans = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        D1[(a, b, c)] = ans
        return ans

D1 = dict()

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")