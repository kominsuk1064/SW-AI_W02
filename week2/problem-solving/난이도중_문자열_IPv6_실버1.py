# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107


add = input()

if "::" in add:
    left, right = add.split("::")

    if left:
        left_part = left.split(":")
    else:
        left_part = []

    if right:
        right_part = right.split(":")
    else:
        right_part = []

    miss = 8 - (len(left_part)) + (len(right_part))

    part = left_part + ["0000"] * miss + right_part

else:
    part = add.split(":")

part = [p.zfill(4) for p in part]

print(":".join(part))