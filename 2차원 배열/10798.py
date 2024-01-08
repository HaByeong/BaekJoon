#나의 풀이
arr_2d = [
    [" " for _ in range(15)]
    for _ in range(15)
]

for i in range(5):
    word = input()
    for j in range(len(word)):
        arr_2d[i][j] = word[j]

for j in range(15):
    for i in range(15):
        if arr_2d[i][j] != " ":
            print(arr_2d[i][j], end = "")

#정석 풀이
#내가 정석이다!