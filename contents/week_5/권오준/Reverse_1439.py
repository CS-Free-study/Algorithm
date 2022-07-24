#백준 1439, 뒤집기, 실버5
import sys
input = sys.stdin.readline

command = input().rstrip()

a = list(filter(None, command.split('0')))
b = list(filter(None, command.split('1')))

print(min(len(a), len(b)))

