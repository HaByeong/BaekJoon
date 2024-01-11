#나의 풀이
x_arr = []
y_arr = []
x_cnt = 0
y_cnt = 0

for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

for i in range(3):
    x_cnt = 0
    y_cnt = 0
    for j in range(3):
        if x_arr[i] == x_arr[j]:
            x_cnt += 1
        if y_arr[i] == y_arr[j]:
            y_cnt += 1
    if x_cnt == 1:
        x = x_arr[i]
    if y_cnt == 1:
        y = y_arr[i]
print(x, y)

#정석 풀이
x_arr = []
y_arr = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in x_arr:
        x_arr.remove(x)
    else:
        x_arr.append(x)
    if y in y_arr:
        y_arr.remove(y)
    else:
        y_arr.append(y)
print(x_arr[0], y_arr[0])