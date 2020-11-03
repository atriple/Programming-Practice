WALL_SYMBOL = '#'
EMPTY_SYMBOL = '.'
ROUTE_SYMBOL = '+'
START_SYMBOL = 'O'
GOAL_SYMBOL = 'X'


class Node():
    """Class Node digunakan untuk menyimpan nilai yang diperlukan pada saat melakukan algoritma searching A*"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, goal):
    """Melakukan algoritma A* untuk mencari rute terpendek pada maze

    Args:
        maze (list(list)): Array 2 dimensi yang terdiri dari angka 1 atau 0
        start (tuple[2]): Posisi start pada maze
        goal (tuple[2]): Posisi goal pada maze

    Returns:
        list(tuple): urutan posisi untuk rute terpendek dari posisi start ke posisi goal       
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = (abs(child.position[0] - end_node.position[0])) + \
                (abs(child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def print_maze_with_path(maze, path=None):
    if path is not None:
        start_position = path.pop(0)
        goal_position = path.pop()
        maze[start_position[0]][start_position[1]] = 2
        maze[goal_position[0]][goal_position[1]] = 3
        for position in path:
            maze[position[0]][position[1]] = 4

    for row in maze:
        row_string = ''
        for val in row:
            if val == 1:
                row_string = row_string + WALL_SYMBOL
            elif val == 2:
                row_string = row_string + START_SYMBOL
            elif val == 3:
                row_string = row_string + GOAL_SYMBOL
            elif val == 4:
                row_string = row_string + ROUTE_SYMBOL
            else:
                row_string = row_string + EMPTY_SYMBOL
            row_string = row_string + ' '
        print(row_string)


def main():
    MAZE = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    START_POSITION = (0, 0)

    GOAL_POSITION = (5, 5)

    if MAZE[START_POSITION[0]][START_POSITION[1]] == 1 or MAZE[GOAL_POSITION[0]][GOAL_POSITION[1]] == 1:
        raise Exception(
            "Posisi start/goal tidak bisa dimasukkan pada daerah yang diblok")

    path = astar(MAZE, START_POSITION, GOAL_POSITION)
    print("Output : ")
    print("Total jarak: {}".format(len(path) - 1))
    print_maze_with_path(MAZE, path)

if __name__ == '__main__':
    main()
