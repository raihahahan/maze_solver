# Maze Solver
## Block Fill
I was bored and created a maze solver for the Block Fill game on https://apps.apple.com/sg/app/offline-games-no-wifi-games/id6448104157.

## How to use
### Installation
1. `git clone https://github.com/raihahahan/maze_solver`
2. `python block_fill.py`

### Usage
1. Play a level on Block Fill

![image](https://github.com/user-attachments/assets/5e969459-fb75-42d5-89a9-89e7872d17d6)

2. Insert the input in the code level
   
![image](https://github.com/user-attachments/assets/232a0bc2-2925-4f12-944c-48a0584e890d)

3. Run `python block_fill.py`
   
4. See the output
   
![image](https://github.com/user-attachments/assets/384e8e49-8767-4cd0-9bc1-082dcb0828c2)

5. Test the output in-game
   
![image](https://github.com/user-attachments/assets/fe9ccf5c-1794-4e12-be68-665abd63982d)

## Technical Explanation: Maze Solver (Hamiltonian Path)

### Overview
The maze solver is designed to find a Hamiltonian path in a maze represented as a 2D grid. A Hamiltonian path is a path that visits every open cell in the maze exactly once. This solver uses a **backtracking algorithm** to explore all possible paths, ensuring every cell is visited without revisiting any.

### Maze Representation
- The maze is represented as a grid where:
  - `"#"` represents a barrier or wall.
  - `" "` (space) represents an open cell that can be traversed.
- The input maze is parsed into a 2D array for processing.

### Algorithm: Backtracking for Hamiltonian Path
The algorithm systematically explores all possible paths through the maze, ensuring:
1. **Validity**: Moves are only made to valid cells (not walls or already visited cells).
2. **Exhaustiveness**: The path continues until all open cells are covered.
3. **Backtracking**: If a dead end is reached, the algorithm backtracks to the previous cell and tries a different path.

#### Key Steps
1. **Initialisation**:
   - Count the total number of open cells (`path_count`).
   - Define movement directions (`up`, `down`, `left`, `right`).
   - Start the search from the first open cell.

2. **Recursive Exploration**:
   - At each step, mark the current cell as visited.
   - Check if the length of the path equals `path_count`. If true, the Hamiltonian path is found.
   - Explore neighboring cells recursively:
     - If a move is valid (within bounds, not a wall, and not visited), proceed to the next cell.
   - If no valid moves remain, backtrack by unmarking the current cell and removing it from the path.

3. **Termination**:
   - The algorithm stops when a Hamiltonian path is found or all possibilities are exhausted.

### Limitations
- The algorithm may not scale efficiently for very large or complex mazes.
- Not all mazes have Hamiltonian paths. The solver will return `None` if no valid path exists.
