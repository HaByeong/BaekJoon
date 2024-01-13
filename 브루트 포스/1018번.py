#나의 풀이 => 못품 엉엉
"""M, N = map(int, input().split())
arr_2d = [
    list(input())
    for _ in range(M)
]

min_cnt = N * M
row = 0

while (8 + row) <= M:
    cnt = 0
    for i in range(row, 8 + row):
        column = 0
        for j in range(column, 8 + column):
            if (8 + column) > N:
                break
            if i % 2 == 0 and j % 2 == 0 and arr_2d[i][j] != arr_2d[row][column]:
                cnt += 1
                arr_2d[i][j] = arr_2d[row][column]
            elif i % 2 == 0 and j % 2 == 1 and arr_2d[i][j] == arr_2d[row][column]:
                cnt += 1
                arr_2d[i][j] = arr_2d[row][column]
            elif i % 2 == 1 and j % 2 == 0 and arr_2d[i][j] == arr_2d[row][column]:
                cnt += 1
                arr_2d[i][j] = arr_2d[row][column]
            elif i % 2 == 1 and j % 2 == 1 and arr_2d[i][j] != arr_2d[row][column]:
                cnt += 1
                arr_2d[i][j] = arr_2d[row][column]
            column += 1
    row += 1
    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)

for row in arr_2d:
    for elem in row:
        print(elem, end = "")
    print()
"""
#정석 풀이
chesscheck = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chesscheck2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
M, N = map(int, input().split())
arr_2d = [
    list(input())
    for _ in range(M)
]
answer = []

for i in range(M - 7):
    for j in range(N - 7):
        cnt = 0
        cnt_2 = 0
        for row in range(8):
            for column in range(8):
                if chesscheck[row][column] != arr_2d[row + i][column + j]:
                    cnt += 1
                if chesscheck2[row][column] != arr_2d[row + i][column + j]:
                    cnt_2 += 1
        answer.append(cnt)
        answer.append(cnt_2)
print(min(answer))









