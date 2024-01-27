import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 연산이 내 풀이가 더 빨라...
while True:
    cnt = 0
    Stack = []
    userInput = input()

    if userInput == ".":
        break
    for word in userInput:
        if word == '(' or word == '[':
            Stack.append(word)
            cnt += 1
        elif word == ')' or word == ']':
            if cnt == 0:
                cnt += 1
                break
            elif word == ')' and Stack[cnt - 1] == '(':
                Stack.pop()
                cnt -= 1
            elif word == ']' and Stack[cnt - 1] == '[':
                Stack.pop()
                cnt -= 1
            else:
                cnt += 1
                break

    if cnt == 0:
        print("yes")
    else:
        print("no")

#정석 풀이
Parenthesis = {')' : '(', ']' : '['}

while True:
    userInput = input()
    if userInput == '.':
        break

    Stack = []
    for word in userInput:
        if word in Parenthesis.values():
            Stack.append(word)
        elif word in Parenthesis.keys():
            if len(Stack) == 0:
                Stack.append(word)
                break
            elif Stack[-1] == Parenthesis[word]:
                Stack.pop()
            elif Stack[-1] != Parenthesis[word]:
                Stack.append(word)
                break
    if len(Stack) == 0:
        print("yes")
    else:
        print("no")

