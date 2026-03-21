# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

k = n - m + 2

for i in range(k - 1):
    print(i, i + 1)

for i in range(k, n):
    print(1, i)