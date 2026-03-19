# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

import sys
input = sys.stdin.readline

N = int(input())

print((1 << N) - 1)

if N <= 20:
    result = []

    def hanoi(n, first, second, third):
        if n == 1:
            result.append(f"{first} {third}")
            return

        hanoi(n - 1, first, third, second)
        result.append(f"{first} {third}")
        hanoi(n - 1, second, first, third)

    hanoi(N, 1, 2, 3)
    print("\n".join(result))