# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

ax = [-1, 1, 0, 0]
ay = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            bx = x + ax[i]
            by = y + ay[i]

            if 0 <= bx < N and 0 <= by < M:
                if maze[bx][by] == 1:
                    maze[bx][by] = maze[x][y] + 1
                    queue.append((bx, by))

bfs()

print(maze[N-1][M-1])