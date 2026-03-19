# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

answer = 0

for p in permutations(A):
    total = 0
    for i in range(N - 1):
        total += abs(p[i] - p[i + 1])
    answer = max(answer, total)

print(answer)