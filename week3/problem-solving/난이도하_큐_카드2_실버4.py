# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

card = deque(range(1, N + 1))

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print (card[0])