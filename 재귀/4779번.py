import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def canto_set(cantoList, x):
    if x == 0:
        return cantoList
    num = 3 ** (x - 1)
    cantoList[num : num * 2] = [" "] * num
    cantoList[:num] = canto_set(cantoList[:num], x - 1)
    cantoList[num * 2:] = canto_set(cantoList[num * 2:], x - 1)
    return cantoList

while True:
    N = input()
    if N == '':
        break
    N = int(N)
    cantoList = ["-"] * (3 ** N)
    canto_set(cantoList, N)
    print("".join(cantoList))