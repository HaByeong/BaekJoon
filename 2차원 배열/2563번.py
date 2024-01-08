#나의 풀이
arr_2d = [
    [0 for _ in range(100)]
    for _ in range(100)
]

n = int(input())
count = 0

for _ in range(n):
    i, j = map(int, input().split())
    for column in range(i, i + 10):
        for row in range(j , j + 10):
            arr_2d[row][column] = 1

for row in arr_2d:
    for elem in row:
        if elem == 1:
            count += 1
print(count)

#정석 풀이
#내가 정석 풀이!!