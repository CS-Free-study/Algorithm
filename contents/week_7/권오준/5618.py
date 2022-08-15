import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = []

for i in range(1, min(nums) + 1):
    if n == 2:
        if nums[0] % i == 0 and nums[1] % i == 0:
            ans.append(i)
    else:
        if nums[0] % i == 0 and nums[1] % i == 0 and nums[2] % i == 0:
            ans.append(i)

for i in ans:
    print(i)