def shortest_path_dfs(graph, src, dest, path=[]):
    path = path + [src]
    if src == dest:
        return path
    
    if src not in graph:
        return None
    
    shortest = None
    for i in graph[src]:
        if i not in path:
            new_path = shortest_path_dfs(graph, i, dest, path)
            if new_path is not None:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

    return shortest


def shortest_path_bfs(graph, src, dest):
    visited = []
    queue = [[src]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]

            for i in neighbours:
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)

                if i == dest:
                    return new_path
            
            visited.append(node)

    return None



# graph = {
#     0: [1, 3],
#     1: [2],
#     3: [4, 7],
#     4: [5, 6, 7],
#     5: [6],
#     6: [7]
# }
graph = {'A': ['B', 'E', 'C'], 
            'B': ['A', 'D', 'E'], 
            'C': ['A', 'F', 'G'], 
            'D': ['B', 'E'], 
            'E': ['A', 'B', 'D'], 
            'F': ['C'], 
            'G': ['C']} 

print(shortest_path_dfs(graph, 'A', 'D'))
print(shortest_path_bfs(graph, 'A', 'D'))