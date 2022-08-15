# DFS

# 얼음 틀의 세로 길이, 가로 길이
n, m = map(int, input().split())

# 얼음 틀 리스트
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 구멍이 뚫려있는 경우(방문 x)
        graph[x][y] = 1 # 방문 처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수
print(result)