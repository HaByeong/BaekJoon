import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
#피보나치 재귀로
def fibo(n):
    global cnt_fibo
    if n == 1 or n == 2:
        cnt_fibo += 1
        return 1
    return fibo(n - 1) + fibo(n - 2)

#피보나치 동적 계획법으로
def fibonacci(n):
    global cnt_fibonacci
    if n == 1 or n == 2:
        return f[n]
    for i in range(3, n + 1):
        f.append(f[i - 1] + f[i - 2])
        cnt_fibonacci += 1


f = [0, 1, 1]
n = int(input())

cnt_fibo = 0
cnt_fibonacci = 0
if n >= 5 and n <= 40:
    fibo(n)
    fibonacci(n)
print(cnt_fibo, end = " ")
print(cnt_fibonacci)

