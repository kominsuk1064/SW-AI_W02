# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [100001] * (k + 1)

dp[0] = 0

for c in coins:
    for i in range(c, k + 1):
        if dp[i - c] != 100001:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])