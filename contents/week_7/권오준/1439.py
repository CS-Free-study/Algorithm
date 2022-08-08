s = input()
a = list(filter(None, s.split('0')))
b = list(filter(None, s.split('1')))
print(min(len(a), len(b)))