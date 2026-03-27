# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (N + 1)
result_dfs = []

def dfs(v):
    visited_dfs[v] = True
    result_dfs.append(v)

    for next_node in graph[v]:
        if not visited_dfs[next_node]:
            dfs(next_node)

dfs(V)

# BFS
visited_bfs = [False] * (N + 1)
result_bfs = []

queue = deque([V])
visited_bfs[V] = True

while queue:
    now = queue.popleft()
    result_bfs.append(now)

    for next_node in graph[now]:
        if not visited_bfs[next_node]:
            visited_bfs[next_node] = True
            queue.append(next_node)

print(*result_dfs)
print(*result_bfs)