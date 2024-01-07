#나의 풀이
score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
sumAll = 0
scoreSum = 0

for _ in range(20):
    arr = input().split()
    if arr[2] == "P":
        continue
    else:
        sumAll += (float(arr[1]) * score[arr[2]])
        scoreSum += float(arr[1])
print(f"{sumAll / scoreSum:6f}")

#정석 풀이
score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
sumAll = 0
scoreSum = 0

for _ in range(20):
    arr = input().split()
    if arr[2] != "P":
        sumAll += (float(arr[1]) * score[arr[2]])
        scoreSum += float(arr[1])
print(f"{sumAll / scoreSum:6f}")