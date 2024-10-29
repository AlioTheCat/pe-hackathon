import numpy as np
from symmetries import generate_all_symmetries

def translate_shape(grid, piece):
    translations = []
    grid_rows, grid_cols = grid.shape
    piece_rows, piece_cols = piece.shape    
    for i in range(grid_rows - piece_rows + 1):
        for j in range(grid_cols - piece_cols + 1):
            window = grid[i:i + piece_rows, j:j + piece_cols]
            if not np.any(window[piece]):  
                new_grid = np.zeros(grid.shape)
                new_grid[i:i + piece_rows, j:j + piece_cols] += piece
                translations.append(new_grid)
    return translations
                
def generate_translations(grid, sym_pieces):
    valid_positions = {}
    for piece_num, symmetries in sym_pieces.items():
        valid_positions[piece_num] = []
        for piece in symmetries:
            valid_positions[piece_num].append(translate_shape(grid, piece))

    return valid_positions

grid = np.array([[1,0,0], [0,0,0], [0,0,0]])
shapes = [np.array([[1, 1], [0, 1]])]
all_sym = generate_all_symmetries(shapes)
print(all_sym)
[print(x) for x in translate_shape(grid, shapes[0])]
