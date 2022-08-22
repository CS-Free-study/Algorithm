import sys
input = sys.stdin.readline

s = input().rstrip()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = len(s)

for i in range(len(s)):
    if s[i: i + 2] in a or s[i: i + 3] in a:
        ans -= 1

print(ans)