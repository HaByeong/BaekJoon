import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 내가 정석인가바
N = int(input())
chatList = set()

chatNum = 0
for _ in range(N):
    chatUser = input()
    if chatUser == "ENTER":
        chatNum += len(chatList)
        chatList.clear()
    else:
        chatList.add(chatUser)

chatNum += len(chatList)
print(chatNum)
