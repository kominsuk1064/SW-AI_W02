# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()

for num in arr:
    left = 0
    right = N - 1
    exist = False

    while left <= right:
        mid = (left + right) // 2
        if num == A[mid]:
            exist = True
            print(1)
            break
        elif num > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if not exist:
        print(0)

