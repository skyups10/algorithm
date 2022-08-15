# BFS : 너비 우선 탐색 알고리즘
# -> 최대한 가까이 있는 노드를 우선으로 탐색
from collections import deque # 큐 사용

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8], 
    [1,7], 
    [1,4,5], 
    [3,5], 
    [3,4], 
    [7], 
    [2,6,8], 
    [1,7] 
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 결과 : 1 2 3 8 7 4 5 6