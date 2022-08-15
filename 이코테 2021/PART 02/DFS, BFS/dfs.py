# DFS : 깊이 우선 탐색 알고리즘
# -> 최대한 멀리 있는 노드를 우선으로 탐색

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 재귀 함수 사용
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



graph = [ # 인접 리스트 방식 사용
    [], # 노드 0 ~ 노드 8에 연결된 노드 정보 저장
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
visited = [False] * 9 # 노드 0 ~ 노드 8

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 결과 : 1 2 7 6 8 3 4 5