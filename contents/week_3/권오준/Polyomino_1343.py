# 백준 1343, 폴리오미노, 실버5
import sys
input = sys.stdin.readline

board = input().rstrip()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

print(-1) if 'X' in board else print(board)  