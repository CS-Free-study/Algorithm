for _ in range(int(input())):
    r, s = map(str, input().split())
    r = int(r)
    p = ""

    for i in range(len(s)):
        p += s[i] * r
    
    print(p)
