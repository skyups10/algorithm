from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 좌 / 우 / 하 / 상
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 현재 위치에서 네 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0: # 괴물이 있는 부분
                continue
            if graph[nx][ny] == 1: # 괴물이 없는 부분
                graph[nx][ny] = graph[x][y] + 1 # 이동 횟수 증가(=최소 칸수, 결과값)
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0)) 

# 괴물이 있는 부분 0 / 괴물이 없는 부분 1
