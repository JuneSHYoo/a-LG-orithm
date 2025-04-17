import sys
import heapq

v ,e =  map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())  
start = k # 지워

graph = [[] for _ in range(v+1)]

for i in range(e):
    u,v, w= map(int, sys.stdin.readline().split())

    graph[u].append((v,w))


def sol(graph, start):
    dist = {i: float('inf') for i in range(0, len(graph))}
    dist[start] = 0

    # 우선순위 큐
    hq = []
    heapq.heappush(hq, [dist[start], start])

    while hq:
        cur_dist, cur_node = heapq.heappop(hq) 

        if dist[cur_node] < cur_dist :
            continue

        g = graph[cur_node]
        for new_node, new_dist in g :
            # print(new_node, new_dist)
            distance = cur_dist + new_dist
            
            if distance < dist[new_node] :
                dist[new_node] = distance
                heapq.heappush(hq, [distance, new_node])
            
    return dist

rest_dist = sol(graph,start)
# print(rest_dist)

for i in range(len(list(rest_dist))-1 ):
    if rest_dist[i+1] == float('inf'):
        print("INF")
    else :
        print(rest_dist[i+1])
    