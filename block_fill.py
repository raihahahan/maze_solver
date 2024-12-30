from collections import deque
from functools import cache

def find_hamiltonian_path(maze, start_r, start_c):
    ROWS, COLS = len(maze), len(maze[0])
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Count total open spaces
    total_open_cells = sum(row.count(" ") for row in maze)

    # Check if a move is valid
    def is_valid(nr, nc, visited):
        return (
            0 <= nr < ROWS and 0 <= nc < COLS and
            maze[nr][nc] == " "  and
            (nr, nc) not in visited
    )

    # Backtracking function
    @cache
    def backtrack(r, c, path):
        if len(visited) == total_open_cells:
            return path  # Found a valid path

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, visited):
                visited.add((nr, nc))
                path += ((nr, nc),)

                result = backtrack(nr, nc, path)
                if result:  # Found a valid path
                    return result

                # Backtrack
                visited.remove((nr, nc))
                path = path[:-1]

        return None  # No path found

    visited = set([(start_r, start_c)])
    path = ((start_r, start_c),)
    return backtrack(start_r, start_c, path)


def solve_maze(maze, start_r, start_c):
    path = find_hamiltonian_path(maze, start_r, start_c)
    if not path:
        print("Path not found.")
        return

    for idx, (r, c) in enumerate(path):
        maze[r][c] = str(idx)
        if idx < 10:
            maze[r][c] = "0" + maze[r][c]

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "#":
                maze[r][c] *= 2
    for row in maze:
        print(" ".join(row))

def generate_maze_string(n, m, barriers):
    # Initialize the maze with empty spaces
    maze = [[" " for _ in range(m)] for _ in range(n)]

    # Place barriers in the maze
    for r, c in barriers:
        if 0 <= r < n and 0 <= c < m:  # Ensure barriers are within bounds
            maze[r][c] = "#"
    return maze

n = 8
m = 6
barriers = [(0,0),(0,3),(2,1),(2,3),(2,4),(3,1),(3,5),(5,2),(5,3),(5,4),(7,2),(7,3)]

start_r = 2
start_c = 2

maze = generate_maze_string(n, m, barriers)
for row in maze:
    print(row)
solve_maze(maze, start_r, start_c)
print(maze)
