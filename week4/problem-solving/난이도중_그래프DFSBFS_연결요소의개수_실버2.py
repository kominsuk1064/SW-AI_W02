# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)