# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

N = int(input())

paper =  [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def origami(x, y, size):
    global white, blue

    color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half = size // 2
                origami(x, y, half)
                origami(x, y + half, half)
                origami(x + half, y, half)
                origami(x + half, y + half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

origami(0, 0, N)

print(white)
print(blue)