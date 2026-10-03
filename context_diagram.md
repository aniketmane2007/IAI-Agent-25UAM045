# C4 Level 1 – Context Diagram

```mermaid
flowchart LR
    U[User] -->|3×3 Puzzle Input| S[3×3 8-Puzzle Solver]
    S -->|Solution / Search Results| U
```

## Explanation
The User provides the initial 3×3 puzzle configuration to the 8-Puzzle Solver. The solver searches for the predefined goal state using BFS or DFS and returns the solution and search-related results to the User.

No external system is required for the basic solver.
