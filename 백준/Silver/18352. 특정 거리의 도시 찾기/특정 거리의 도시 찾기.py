from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

graph = list([] for _ in range(n+1))

distance = [-1]*(n+1)
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


# 최단 거리 탐색 시작
def sol(x) :
    q = deque([x])
    distance[x] = 0 
    visited[x] = True

    while q :
        cur = q.popleft()
        # print(cur)
        for next_node in graph[cur] :
            if distance[next_node] == -1 :
                distance[next_node] = distance[cur] + 1
                visited[next_node] = True
                q.append(next_node)

                # print(next_node)
                # print(">> v: " , visited)
                # print(">> d: " , distance)

sol(x)

if k not in distance :
    print(-1)
else :
    for i, val in enumerate(distance):
        if val == k:
            print(i)
