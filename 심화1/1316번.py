# 나의 풀이 -> 맞춤
#문자열 끼리 비교시 슬라이싱!
n = int(input())
cnt = 0

for _ in range(n):
    string = input()
    numCheck = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            for j in range(i + 2, len(string)):
                if string[i] == string[j]:
                    numCheck = -1
    if numCheck == 0:
        cnt += 1
print(cnt)

# 정석 풀이 -> find()를 이용하라!
n = int(input())
cnt = n

for _ in range(n):
    word = input()
    for i in range(len(word) - 1):
        if word.find(word[i]) > word.find(word[i + 1]):
            cnt -= 1
            break
print(cnt)



