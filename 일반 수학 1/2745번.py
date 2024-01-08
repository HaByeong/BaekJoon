#나의 풀이 대문자 아스키 코드 65~~
arr, n = input().split()

n = int(n)
sum_val = 0
listLen = len(arr)

for i in range(listLen):
    if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
        sum_val += (ord(arr[i]) - 55) * (n ** (listLen - i - 1))
    else:
        sum_val += int(arr[i]) * (n ** (listLen - i - 1))
print(sum_val)

#정석 풀이 int(변환할 string or 숫자, n진법) 이 가능!!
arr, n = input().split()
n = int(n)
answer = int(arr, n)
print(answer)
