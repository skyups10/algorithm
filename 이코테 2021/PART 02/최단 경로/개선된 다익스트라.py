# 개선된 다익스트라 알고리즘
# get_smallest_node() 함수 작성할 필요 없음
# -> 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수에서 우선순위 큐를 이용하는 방식으로 대체 가능하기 때문

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input()) # 시작 노드 번호
distance = [INF] * (n+1) # 최단 거리 테이블(결과)

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1): # 모든 노드로 가기 위한 최단 거리 출력
    if distance[i] == INF: # 도달할 수 없는 경우
        print("INFINITY")
    else: # 도달할 수 있는 경우
        print(distance[i])