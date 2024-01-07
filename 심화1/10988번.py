# 내가 푼 것
arr = input()
arr2 = arr[::-1]

if arr == arr2:
    print(1)
else:
    print(0)


#정석 풀이
arr = input()

if arr == arr[::-1]:
    print(1)
else:
    print(0)