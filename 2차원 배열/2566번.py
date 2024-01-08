#나의 풀이
"""arr_2d = [
    list(map(int, input().split()))
    for _ in range(9)
]

maxValue = arr_2d[0][0]
maxRow = 0
maxColumn = 0

for i in range(9):
    for j in range(9):
        if arr_2d[i][j] > maxValue:
            maxValue = arr_2d[i][j]
            maxRow, maxColumn = i, j
print(maxValue)
print(f"{maxRow + 1} {maxColumn + 1}")
"""
#정석 풀이 -> 입력 받으면서 판단하기
maxValue = 0
maxRow = 0
maxColumn = 0
# 1. 9개 라인을 입력받아서
for i in range(1, 10):
    L = list(map(int, input().split()))
    if max(L) >= maxValue:
        maxValue = max(L)
        maxRow, maxColumn = i, L.index(max(L))
print(maxValue)
print(maxRow, maxColumn + 1)


