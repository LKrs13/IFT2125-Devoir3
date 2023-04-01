# https://www.programiz.com/dsa/ford-fulkerson-algorithm
def searching_algo_BFS(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while searching_algo_BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Adding the path flows
        max_flow += path_flow

        # Updating the residual values of edges
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

# graph = [[0, 8, 0, 0, 3, 0],
#          [0, 0, 9, 0, 0, 0],
#          [0, 0, 0, 0, 7, 2],
#          [0, 0, 0, 0, 0, 5],
#          [0, 0, 7, 4, 0, 0],
#          [0, 0, 0, 0, 0, 0]]

# source = 0
# sink = 5

# print("Max Flow: %d " % ford_fulkerson(graph, source, sink))