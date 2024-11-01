from symmetries import generate_all_symmetries
from translation import generate_translations
from exploit_solution import flatten
import numpy as np
import matplotlib.pyplot as plt
from xcover import covers_bool
from exploit_solution import piece_matx_list, piece_flattened_list, convert_solution_to_matx

RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}


grid= np.zeros((8,8))
grid[3:5,3:5] += 1
shapes=list(map(np.array, RAW_SHAPES.values()))


def solve_puzzle(grid, shapes):
    h,w=grid.shape
    N=len(shapes)
    symetries = generate_all_symmetries(shapes)
    pos = generate_translations(grid,symetries)
    mat_list = piece_matx_list(pos)
    vect_list_flat = np.array(piece_flattened_list(N,pos,grid))

    try:
        solution = next(covers_bool(vect_list_flat))
    except StopIteration:
        print("NO SOLUTIONS WERE FOUND")
        return 
    M = convert_solution_to_matx(solution, vect_list_flat, mat_list, N, h,w)
    M += 1.4*N*grid
    plt.matshow(M, cmap='terrain')
    plt.show()


solve_puzzle(grid, shapes)







