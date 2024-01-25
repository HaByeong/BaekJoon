import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())

stack = []

for _ in range(N):
    userInput = list(input().split())
    if userInput[0] == '1':
        stack.append(userInput[1])
    elif userInput[0] == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif userInput[0] == '3':
        print(len(stack))
    elif userInput[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif userInput[0] == '5':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

# 정석 풀이 -> 삼중 연산자 사용 근데 이게 더 시간이 많이 걸림 ;;
N = int(input())

stack, Len = [], 0
for _ in range(N):
    userInput = list(input().split())
    if userInput[0] == '1':
        stack.append(userInput[1])
        Len += 1
    elif userInput[0] == '2':
        print(-1 if (Len == 0) else stack.pop())
        Len = max(Len - 1, 0)
    elif userInput[0] == '3':
        print(Len)
    elif userInput[0] == '4':
        print(1 if (Len == 0) else 0)
    elif userInput[0] == '5':
        print(-1 if (Len == 0) else stack[-1])









