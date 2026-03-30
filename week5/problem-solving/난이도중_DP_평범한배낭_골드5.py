# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

dp = [0] * (K + 1)

for _ in range(N):
    weight, value = map(int, input().split())

    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[K])