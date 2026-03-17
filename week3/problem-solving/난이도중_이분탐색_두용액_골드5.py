# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

## 이분탐색
N = int(input())
solution = list(map(int, input().split()))

solution.sort() # 이분탐색을 사용하기 위해 정렬

answer = float('inf')   # 현재까지 찾은 합(0과의 차이가 가장 작은 값)
left_answer = 0     # 정답 용액 1
right_answer = 0    # 정답 용액 2    

for i in range(N - 1):  # 첫 번째 용액을 하나 고정

    left = i + 1    # i 이후 구간에서 두 번째 용액을 찾기 위해 이분탐색 수행
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        current_sum = solution[i] + solution[mid]   # 두 용액의 합

        if abs(current_sum) < abs(answer):  # 현재 합이 기존보다 0에 더 가깝다면 정답 갱신
            answer = current_sum
            left_answer = solution[i]
            right_answer = solution[mid]

        if current_sum < 0:     # 합이 양수라면 값을 줄여야 하므로 왼쪽 탐색
            left = mid + 1
        else:
            right = mid - 1

print(left_answer, right_answer)





## 투 포인터

N = int(input())
solution = list(map(int, input().split()))

solution.sort()

left = 0
right = N - 1

answer_sum = float('inf')   # 현재까지 가장 0에 가까운 합
left_answer = 0
right_answer = 0

while left < right:     # 두 포인터가 만날 때까지 반복
    current_sum = solution[left] + solution[right]

    if abs(current_sum) < abs(answer_sum):      # 현재 합이 기존보다 0에 더 가깝다면 갱신
        answer_sum = current_sum
        left_answer = solution[left]
        right_answer = solution[right]

    if current_sum < 0:     # 합이 음수이면 더 큰 값을 만들기 위해 right 이동
        left += 1
    elif current_sum > 0:   # 합이 양수이면 값을 줄이기 위해 right 이동
        right -= 1
    else:                   # 합이 0이면 더 좋은 답이 없으므로 종료
        break

print(left_answer, right_answer)
