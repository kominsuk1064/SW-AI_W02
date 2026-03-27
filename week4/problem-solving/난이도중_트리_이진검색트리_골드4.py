# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

def postorder(start, end):
    if start > end:
        return

    root = preorder[start]

    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)

postorder(0, len(preorder) - 1)