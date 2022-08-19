# Python 3는 시간 초과 / PyPy3은 통과

import sys
input = sys.stdin.readline

# 0 : 빈칸 / 1 : 벽 / 2 : 바이러스
n, m = map(int, input().split())

data = [] # 벽 설치 전의 맵
for _ in range(n):
    data.append(list(map(int, input().split())))

temp = [[0] * m for _ in range(n)] # 벽 설치 후의 맵

#    좌  우  상  하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS 이용하여 각 바이러스 퍼지게 하는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2 # 바이러스 전파
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: # 빈칸(=안전 영역)
                score += 1
    return score

# DFS 이용하여 울타리 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result # 전역 변수
    if count == 3: # 울타리 3개 설치된 경우
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] # 1) 울타리 설치 전과 후의 맵 동일하게 적용
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2: # 2) 바이러스 전파
                    virus(i, j)
        result = max(result, get_score()) # 3) 안전 영역 크기
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1 # 방문 처리
                count += 1 # 울타리 생성
                dfs(count)
                # 재귀가 끝나면 울타리 개수는 최대이기 때문에 다시 원상복구
                data[i][j] = 0 # 미방문 처리
                count -= 1 # 울타리 삭제

dfs(0)
print(result)