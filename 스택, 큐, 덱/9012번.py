import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> () 완성되면 빼버리면 되자않나
T = int(input())

for _ in range(T):
    Stack = []
    Len = 0
    String = list(input())
    for i in range(len(String)):
        if String[i] == '(':
            Stack.append(String[i])
            Len += 1
        elif String[i] == ')' and Len == 0:
            Stack.append(String[i])
            Len += 1
        elif String[i] == ')' and Stack[Len - 1] == '(':
            Stack.pop()
            Len -= 1
        else:
            Stack.append(String[i])
            Len += 1
    print("NO" if (len(Stack) != 0) else "YES")


