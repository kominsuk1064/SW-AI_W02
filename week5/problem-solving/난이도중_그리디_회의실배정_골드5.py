# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)