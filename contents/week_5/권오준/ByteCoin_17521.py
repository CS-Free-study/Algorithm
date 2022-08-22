# 백준 17521, Byte Coin, 실버4
import sys
input = sys.stdin.readline

n, money = map(int, input().split())
cost = [int(input()) for _ in range(n)]

coin = 0

for i in range(n - 1):
    if cost[i] < cost[i + 1]:
        if money // cost[i] > 0:
            coin = money // cost[i]
            money -= coin * cost[i]
        if money < 0:
            money = 0
    elif cost[i] > cost[i + 1]:
        money += coin * cost[i]
        coin = 0
    #print("coin: {0}, money: {1}".format(coin, money))

if coin:
    money += coin * cost[-1]

print(money)