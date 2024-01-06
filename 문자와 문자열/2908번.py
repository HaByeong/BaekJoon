first_num, second_num = input().split()

first_num = int(first_num[::-1])
second_num = int(second_num[::-1])

if first_num >= second_num:
    print(first_num)
else:
    print(second_num)

