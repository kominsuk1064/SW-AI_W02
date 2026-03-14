# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

N = int(input())
solution = list(map(int, input().split()))

solution.sort()

left = 0
right = N - 1

answer_sum = float('inf')
left_answer = 0
right_answer = 0

while left < right:
    current_sum = solution[left] + solution[right]

    if abs(current_sum) < abs(answer_sum):
        answer_sum = current_sum
        left_answer = solution[left]
        right_answer = solution[right]

    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(left_answer, right_answer)