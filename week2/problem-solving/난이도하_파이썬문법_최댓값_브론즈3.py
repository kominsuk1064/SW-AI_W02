# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

arr = []

for _ in range(9):
    arr.append(int(input()))

max_value = max(arr)
index = arr.index(max_value) + 1

print(max_value)
print(index)