import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def generate_maze(size):
    maze = np.random.choice([0, 1, 2, 3, 4, 5], size=(size, size), p=[0.5, 0.2, 0.05, 0.1, 0.1, 0.05])  
    maze[0, 0] = 0  
    maze[size-1, size-1] = 0  
    return maze
 
def get_cell_properties(cell_type):
    cell_properties = {
        0 : {"Time_cost" : 1, "Score" : 0},
        1 : {"Time_cost" : float('inf'), "Score" : None},
        2 : {"Time_cost" : 3, "Score" : -1},
        3 : {"Time_cost" : 5, "Score" : -3},
        4 : {"Time_cost" : 0.5, "Score" : 2},
        5 : {"Time_cost" : 0.1, "Score" : 1},
    }
    return cell_properties[cell_type]

def draw_maze(maze):
    cmap = mcolors.ListedColormap(["white", "black", "darkgreen", "red", "blue", "purple"])
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap=cmap, origin="upper")
    plt.xticks([]), plt.yticks([])
    plt.show()

size = int(input("Enter size maze: "))
maze = generate_maze(size)
draw_maze(maze)

for i in range(size):
    for j in range(size):
        cell_type = maze[i,j]
        time_cost, score = get_cell_properties(cell_type).values()
        print(f"Cell: ({i}, {j}) - Type: {cell_type}, Time Cost: {time_cost}, Score: {score}")