# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Aniket Anandrao Mane  
**PRN:** 25UAM045  
**System:** 3×3 8-Puzzle Solver using BFS and DFS

## Purpose
This folder contains the SLE-3 architectural documentation for the 3×3 8-Puzzle Solver. The architecture is represented using all four C4 levels: Context, Container, Component and Code.

The system accepts a puzzle configuration, searches for the goal state using BFS and DFS, manages visited states, and produces solution/search results.

## SLE-2 Connection
The architecture continues the search-system work from SLE-2 and separates input, puzzle-state handling, search, visited-state management and output responsibilities.

## C4 Levels
1. Context – system and user interaction.
2. Container – major building blocks inside the solver.
3. Component – internal parts of the Search Engine.
4. Code – important functions/classes used by the implementation.
