# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)

queue = deque([1])

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if parent[next_node] == 0 and next_node != 1:
            parent[next_node] = now
            queue.append(next_node)

for i in range(2, N + 1):
    print(parent[i])