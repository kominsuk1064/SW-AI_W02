# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())

turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

row = [0, 1, 0, -1]
columns = [1, 0, -1, 0]
direction = 0

snake = deque()
snake.append((0, 0))

time = 0
head_row, head_columns = 0, 0

while True:
    time += 1
    now_row = head_row + row[direction]
    now_columns = head_columns + columns[direction]

    if not (0 <= now_row < N and 0 <= now_columns < N):
        break

    if (now_row, now_columns) in snake:
        break

    snake.append((now_row, now_columns))

    if board[now_row][now_columns] == 1:
        board[now_row][now_columns] = 0
    else:
        snake.popleft()

    head_row, head_columns = now_row, now_columns

    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)