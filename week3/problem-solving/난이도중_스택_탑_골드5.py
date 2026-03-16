# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

N = int(input())
height = list(map(int, input().split()))

stack = []
answer = []

for i in range(N):
    while stack and stack[-1][1] < height[i]:
        stack.pop()

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0])

    stack.append((i + 1, height[i]))

print(*answer)