# Input
ISLAND_MAP = ((1, 1, 0, 0, 0),
              (0, 1, 0, 0, 1),
              (1, 0, 0, 1, 1),
              (0, 0, 0, 0, 0),
              (1, 0, 1, 0, 1))


def search_island(island_map):
    """Search for island

    Args:
        ...

    Returns:
        int: number of island(s)
    """

    # TODO: Make it more efficient with caching
    # TODO: Make it more functional/declarative
    # TODO: Handle exceptions

    map_size = {"row": len(island_map), "col": len(island_map[0])}
    visited_node = [[0] * map_size["col"]] * map_size["row"]
    island_count = 0

    def depth_first_search(island_map, visited_node, row, col):
        map_size = {"row": len(island_map), "col": len(island_map[0])}
        print(visited_node)
        print(row, col)
        visited_node[row][col] = 1
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                adjacent_row = row + i
                adjacent_col = col + j
                isRowInBound = adjacent_row >= 0 and adjacent_row < map_size["row"]
                isColInBound = adjacent_col >= 0 and adjacent_col < map_size["col"]

                if not(isRowInBound) or not(isColInBound):
                    continue
                 
                if island_map[adjacent_row][adjacent_col] and not(visited_node[adjacent_row][adjacent_col]):
                    print(adjacent_row, adjacent_col)
                    depth_first_search(island_map, visited_node, adjacent_row, adjacent_col)

        return visited_node

    for row in range(map_size["row"]):
        for col in range(map_size["col"]):
            if island_map[row][col] and not(visited_node[row][col]):
                visited_node = depth_first_search(island_map, visited_node, row, col)
                print("d", visited_node)
                island_count = island_count + 1
    
    return island_count

print("Output: {}".format(search_island(ISLAND_MAP)))