# SLE-3 Submission Content

## 1. System Title & Short Description

### 3×3 8-Puzzle Solver using BFS and DFS

The 3×3 8-Puzzle Solver accepts an initial puzzle configuration from the user. It represents the blank space using `0` and searches for the predefined goal state. The system uses Breadth-First Search (BFS) and Depth-First Search (DFS) to find a solution. It manages visited puzzle states to avoid unnecessary repeated searches. The system displays the solution and search-related results for comparison.

## 2. Context Diagram – Level 1

The User supplies the initial puzzle state to the 3×3 8-Puzzle Solver. The system performs the search and returns the solution and search results.

## 3. Container Diagram – Level 2

- **Input Module:** accepts and prepares puzzle input.
- **Puzzle State Manager:** represents states and generates valid moves.
- **Search Engine:** executes BFS or DFS.
- **Visited / State Manager:** tracks explored states.
- **Output Module:** displays the solution and results.

## 4. Component Diagram – Level 3

The Search Engine is expanded because it is the main algorithmic part of the system. BFS Search and DFS Search use frontier management, goal testing and visited-state handling before path reconstruction.

## 5. Code Level Overview – Level 4

Important implementation functions include input handling, solvability checking, neighbor generation, BFS, DFS, grid display and performance measurement.

## 6. Design Decisions

The system is divided into input, puzzle-state management, search, visited-state management and output responsibilities to keep the architecture simple and readable. BFS and DFS are kept as separate search implementations so their behavior and performance can be compared using the same puzzle input. Only the Search Engine is expanded at the Component level to keep the C4 model within the required scope.

## 7. AI Contribution Note

**AI tool used:** ChatGPT

**AI helped with:** understanding the Full C4 Model, organizing the architecture into the four required levels, preparing documentation structure and checking whether the design followed the SLE-3 guideline.

**My contribution:** I selected the 3×3 8-Puzzle system, worked on the BFS/DFS implementation and testing, performed the SLE-2 experiments, reviewed the architecture and will verify the final diagrams and implementation details before submission.

## 8. Conclusion

The Full C4 architecture shows the 3×3 8-Puzzle Solver from system context down to important code-level functions. The design connects the implementation and performance work from the earlier SLEs with a clear architectural structure.
