#나의 풀이
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    if num2 % num1 == 0:
        print("factor")
    elif num1 % num2 == 0:
        print("multiple")
    else:
        print("neither")

#정석 풀이
#나의 풀이가 정석