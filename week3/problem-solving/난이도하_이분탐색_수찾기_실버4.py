# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

N = int(input())
A = list(map(int, input().split())) # input()으로 한 줄을 입력받고, split()으로 공백 기준으로 나눈 다음, map(int)으로 문자열을 정수로 변환하고, list()로 리스트로 만들기
M = int(input())
arr = list(map(int, input().split()))

A.sort()    # A 정렬

for num in arr:     # arr의 각 원소별로 이분탐색
    left = 0
    right = N - 1
    exist = False   # 숫자 존재 여부

    while left <= right:    # 탐색 범위가 존재할 때까지
        mid = (left + right) // 2   # 중간 인덱스
        if num == A[mid]:           # 값을 찾은 경우
            exist = True
            print(1)
            break   # 반복문 탈출
        elif num > A[mid]:  # 찾는 값이 더 크면 오른쪽 탐색
            left = mid + 1
        else:               # 찾는 값이 더 작으면 왼쪽 탐색
            right = mid - 1

    if not exist:   # 목표값을 찾지 못했다면
        print(0)

