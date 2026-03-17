# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque   # 양쪽에서 빠르게 삽입/삭제 가능한 deque 사용

N = int(input())    # 보드 크기
K = int(input())    # 사과 개수

board = [[0] * N for _ in range(N)]     # 보드 생성(0: 빈칸, 1: 사과)

for _ in range(K):          # 사과 위치 입력
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())    # 방향 전환 횟수

turns = {}              # 시간별 방향 전환 정보 저장
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C   # X초 후 C 방향으로 회전   

# 방향(오른쪽, 아래 왼쪽, 위)
row = [0, 1, 0, -1]
columns = [1, 0, -1, 0]
direction = 0   # 처음 방향 오른쪽

snake = deque()
snake.append((0, 0))            # 뱀 시작 위치

time = 0
head_row, head_columns = 0, 0   # 뱀 머리 위치

while True:     # 매 초마다 이동
    time += 1   # 시간 증가

    # 다음 위치 계산(현재 방향 기준)
    now_row = head_row + row[direction]
    now_columns = head_columns + columns[direction]

    # 벽에 부딪히면 게임 종료
    if not (0 <= now_row < N and 0 <= now_columns < N):
        break

    # 자기 몸에 부딪히면 게임 종료
    if (now_row, now_columns) in snake:
        break

    # 머리를 새로운 위치로 이동
    snake.append((now_row, now_columns))

    # 사과가 있는 경우 꼬리 유지
    if board[now_row][now_columns] == 1:
        board[now_row][now_columns] = 0
    else:   # 사과가 없는 경우 꼬리 제거
        snake.popleft()

    head_row, head_columns = now_row, now_columns   # 머리 위치 업데이트

    # 방향 전환 시간이면 방향 변경
    if time in turns:
        if turns[time] == 'D':      # 오른쪽 화면
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)