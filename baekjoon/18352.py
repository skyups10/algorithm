import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 특정한 도시 x로부터 출발하여 도달할 수 있는 최단 거리 리스트
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    v = q.popleft()
    for next_node in graph[v]:
        if distance[next_node] == -1: # 방문하지 않은 도시라면
            distance[next_node] = distance[v] + 1
            q.append(next_node)
        
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
