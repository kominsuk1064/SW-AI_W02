# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())

passwords = []

for _ in range(N):
    passwords.append(input())

for c in passwords:
    if c[::-1] in passwords:
        print(len(c), c[len(c)//2])
        break