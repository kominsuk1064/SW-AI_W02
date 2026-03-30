# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    volunteer = [tuple(map(int, input().split())) for _ in range(N)]
    
    volunteer.sort()
    
    count = 1
    min_interview = volunteer[0][1]
    
    for i in range(1, N):
        if volunteer[i][1] < min_interview:
            count += 1
            min_interview = volunteer[i][1]
    
    print(count)