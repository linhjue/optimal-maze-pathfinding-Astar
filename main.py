import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def generate_maze(size):
    maze = np.random.choice([0, 1, 2, 3, 4, 5], size=(size, size), p=[0.5, 0.2, 0.05, 0.1, 0.1, 0.05])  
    maze[0, 0] = 0  
    maze[size-1, size-1] = 0  
    return maze
 
def draw_maze(maze):
    cmap = mcolors.ListedColormap(["white", "black", "darkgreen", "red", "blue", "purple"])
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap=cmap, origin="upper")
    plt.xticks([]), plt.yticks([])
    plt.show()

size = int(input("Enter size maze: "))
maze = generate_maze(size)
draw_maze(maze)
