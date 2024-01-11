#나의 풀이
x, y, w, h = map(int, input().split())

arr = [x - 0, y - 0, w - x, h - y]
print(min(arr))

#정석 풀이
x, y, w, h = map(int, input().split())

arr = [x, y, w - x, h - y] #이걸.. 나는..
print(min(arr))
