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


grid= np.zeros((5,12))
shapes=list(map(np.array, RAW_SHAPES.values()))


def solve_puzzle(grid, shapes):
    h,w=grid.shape
    N=len(shapes)
    symetries = generate_all_symmetries(shapes)
    pos = generate_translations(grid,symetries)
    mat_list = piece_matx_list(pos)
    vect_list_flat = np.array(piece_flattened_list(N,pos,grid))
    print(vect_list_flat)
    solution = next(covers_bool(vect_list_flat))
    M = convert_solution_to_matx(solution, vect_list_flat, mat_list, N, h,w)
    # print(M)
    plt.matshow(M, cmap='magma')
    plt.show()


solve_puzzle(grid, shapes)







