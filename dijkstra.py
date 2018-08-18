""" Здесь представлен алгоритм дейкстры """


def dijkstra(w, dist, used, start_node):
    dist[start_node] = 0
    min_dist = 0
    min_vertex = start_node

    while min_dist < float('inf'):
        i = min_vertex
        used[i] = True
        for j in range(len(dist)):
            if dist[i] + w[i][j] < dist[j]:
                dist[j] = dist[i] + w[i][j]
        min_dist = float('inf')
        for j in range(len(dist)):
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j
    return dist





if __name__ == '__main__':
    w = [
        [0, 5, 2, float('inf'), 15], 
        [5, 0, 1, 3, float('inf')], 
        [2, 1, 0, float('inf'), 4], 
        [float('inf'), 3, float('inf'), 0, 12], 
        [15, float('inf'), 4, 12, 0]
    ]
    dist = [float('inf')] * len(w)
    used = [False] * len(w)

    result = dijkstra(w, dist, used, 0)
    print(result)
