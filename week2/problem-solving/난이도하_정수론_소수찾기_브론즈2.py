# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


n = int(input())
nums = list(map(int, input().split()))

count = 0

for num in nums:
    if num < 2:
        continue
    
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        count += 1

print(count)