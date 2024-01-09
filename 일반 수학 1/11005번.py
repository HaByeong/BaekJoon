#나의 풀이
N, B = map(int, input().split())
arr = []

while True:
    arr.append(N % B)
    N //= B
    if N == 0: #몫이 0이 되면
        break

arr = arr[::-1]
for i in range(len(arr)):
    if arr[i] >= 10 and arr[i] <= 35:
        arr[i] = chr(arr[i] + 55)
    print(arr[i], end = "")

#정석 풀이
N, B = map(int, input().split())
List = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Str = ''
while N != 0:
    Str += List[N % B]
    N //= B
print(Str[::-1])
