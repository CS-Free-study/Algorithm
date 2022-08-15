s = input()
a = [chr(i + 97) for i in range(26)]
ans = []
for i in range(26):
    print(s.find(a[i]), end = ' ')