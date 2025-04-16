n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(i, depth) :
    global arrive 

    # print("depth", depth)
    # print("now: ", i)
    # print(visited )
    
    if depth == 5 :
        arrive = True
        return 

    for n in graph[i] :
        if visited[n] == False :
            visited[n] = True
            dfs(n, depth + 1)
            visited[n] = False

arrive = False
for i in range(n):
    # print("start with" , i)
    visited = [False]*(n)
    visited[i] = True
    dfs(i,1)
    if arrive :
        break

if arrive :
    print(1)
else :
    print(0)