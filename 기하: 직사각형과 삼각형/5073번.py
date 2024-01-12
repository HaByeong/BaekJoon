#나의 풀이
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    elif a >= b + c or b >= a + c or c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

#정석 풀이(좀 더 깔끔한 코드)
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == b == c:
        print('Equilateral')
    elif a + b <= c or b + c <= a or c + a <= b:
        print('Invalid')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')