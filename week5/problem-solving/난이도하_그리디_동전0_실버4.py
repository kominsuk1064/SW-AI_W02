# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0

for coin in reversed(coins):
    count += K // coin
    K %= coin

print(count)