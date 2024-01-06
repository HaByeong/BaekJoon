dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

string = input()
time = 0

for word in dial:
    for i in string:
        if i in word:
            time = time + (dial.index(word) + 3)

print(time)


