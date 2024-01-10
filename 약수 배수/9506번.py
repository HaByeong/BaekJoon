#나의 풀이
while True:
    n = int(input())
    sum_val = 0
    cnt = 0
    arr = []
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            sum_val += i
            arr.append(i)

    if sum_val == n:
        print(f"{n} = ", end = "")
        for word in arr:
            print(word, end = "")
            cnt += 1
            if cnt < len(arr):
                print(" + ", end = "")
        print()
    else:
        print(f"{n} is NOT perfect.")

#정석 풀이



