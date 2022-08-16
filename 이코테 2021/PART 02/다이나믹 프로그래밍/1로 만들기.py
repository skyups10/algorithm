# 해당 문제와 매우 유사 : https://www.acmicpc.net/problem/1463
# 보텀업 다이나믹 프로그래밍

x = int(input())
d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])