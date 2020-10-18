# Input
ISLAND_MAP = ((1, 1, 0, 0, 0),
              (0, 1, 0, 0, 1),
              (1, 0, 0, 1, 1),
              (0, 0, 0, 0, 0),
              (1, 0, 1, 0, 1))


def search_island(island_map):
    """Search for island from given map

    Args:
        island_map (tuple<tuple>) : 2 dimensional array consist of 1 or 0's

    Returns:
        int: number of island(s)
    """

    # TODO: Make it more efficient with caching
    # TODO: Handle exceptions

    MAP_SIZE = {"row": len(island_map), "col": len(island_map[0])}
    visited_node = [[0] * MAP_SIZE["col"] for _ in range(MAP_SIZE["row"])] 
    island_count = 0

    def depth_first_search(island_map, visited_node, row, col, map_size=MAP_SIZE):
        visited_node[row][col] = 1
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                adjacent_row = row + i
                adjacent_col = col + j
                isRowNotInBound = adjacent_row < 0 or adjacent_row >= MAP_SIZE["row"]
                isColNotInBound = adjacent_col < 0 or adjacent_col >= MAP_SIZE["col"]

                if isRowNotInBound or isColNotInBound:
                    continue
                 
                if island_map[adjacent_row][adjacent_col] and not(visited_node[adjacent_row][adjacent_col]):
                    depth_first_search(island_map, visited_node, adjacent_row, adjacent_col)

        return visited_node

    for row in range(MAP_SIZE["row"]):
        for col in range(MAP_SIZE["col"]):
            if island_map[row][col] and not(visited_node[row][col]):
                visited_node = depth_first_search(island_map, visited_node, row, col)
                island_count = island_count + 1
    
    return island_count

print("Output: {}".format(search_island(ISLAND_MAP)))