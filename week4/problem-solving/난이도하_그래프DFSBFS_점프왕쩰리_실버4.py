# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
queue = deque()
queue.append((0, 0))
visited[0][0] = True

while queue:
    r, c = queue.popleft()

    if board[r][c] == -1:
        print("HaruHaru")
        break

    jump = board[r][c]

    nr, nc = r + jump, c
    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
        visited[nr][nc] = True
        queue.append((nr, nc))

    nr, nc = r, c + jump
    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
        visited[nr][nc] = True
        queue.append((nr, nc))

else:
    print("Hing")