# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

import sys
input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]

U.sort()

absum = set()

for i in range(N):
    for j in range(N):
        absum.add(U[i] + U[j])

for i in range(N-1, -1, -1):
    d = U[i]
    for j in range(N):
        c= U[j]
        if d - c in absum:
            print(d)
            exit()