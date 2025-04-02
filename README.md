# Optimal Pathfinding in a Maze - A* Algorithm

## Introduction
This project implements the A* algorithm to find the shortest path and highest points in a maze. In addition to finding the path, we also include elements such as monsters, swamps, gems, and power-up zones to simulate a dungeon full of challenges.

## Game Rules

| Cell Type        | Score | Time Cost | Color       |
|------------------|-------|-----------|-------------|
| Normal Path      | 0     | 1         | White       |
| Wall             | X     | X         | Black       |
| Swamp            | -1    | 3         | Dark Green  |
| Monster          | -3    | 5         | Red         |
| Gem              | +2    | 0.5       | Blue        |
| Power-Up Zone    | +1    | 0.1       | Purple      |

## Installation

### Requirements
- Python 3.x
- NumPy, Matplotlib libraries

### How to Install Libraries
Run the following command in your terminal:
```bash
pip install numpy matplotlib
```

### How to Run
```bash
python main.py
```

### Sample Results 

### Lesson Learned
- A* is an optimal search algorithm.
- Adding dungeon element increases the complexity of the problem.
