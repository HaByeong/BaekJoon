#내가 푼 거
croAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()
cnt = 0

for i in range(len(croAlpha)):
    if croAlpha[i] in string:
        cnt += string.count(croAlpha[i])
        string = string.replace(croAlpha[i], " ")

for word in string:
    if word != " ":
        cnt += 1

print(cnt)

#정석 풀이
croAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()
cnt = 0

for i in range(len(croAlpha)):
    if croAlpha[i] in string:
        cnt += string.count(croAlpha[i])
        string = string.replace(croAlpha[i], " ")

string = string.replace(" ", "")
cnt += len(string)

print(cnt)


