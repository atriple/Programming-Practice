graph = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'E'],
         'D': ['B', 'E', 'F'],
         'E': ['C', 'D', 'F'],
         'F': ['D', 'E']}

def bfs(graph, start, end):
  visited = [start]
  queue = [start]
  hierarchy = {start: None}

  while len(queue) > 0:
    current = queue.pop(0)

    if current == end:
      path = [end]
      child = end
      while start not in path:
        path = [hierarchy[child]] + path
        child = hierarchy[child]
      return path
      
    for node in graph[current]:
      if node not in visited:
        visited += [node]
        queue += [node]
        hierarchy[node] = current

path = bfs(graph, "A", "F")
print(path) # Output : ['A', 'B', 'D', 'F']