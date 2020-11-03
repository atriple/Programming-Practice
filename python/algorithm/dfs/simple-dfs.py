graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'E'],
         'D': ['B', 'E', 'F'],
         'E': ['C', 'D', 'F'],
         'F': ['D', 'E']}


def dfs(graph, start, end, path=[], visited=[]):
    """Return """
    if start in visited:
        return path
        
    path += [start]
    visited += [start]

    if start == end:
      return path
    for edge in graph[start]:
        if edge not in visited:
            return dfs(graph,edge,end,path,visited)

path = dfs(graph, "A", "F")
print(path) # Output : ['A', 'B', 'C', 'E', 'D', 'F']
