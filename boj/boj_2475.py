# 2475번 검증수

tot = 0
arr = list(map(int, input().split()))
for num in arr:
    tot += pow(num, 2)
print(tot%10)