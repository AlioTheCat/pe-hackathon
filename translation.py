import numpy as np
from symmetries import generate_all_symmetries

def translate_shape(grid, piece):
    translations = []
    grid_rows, grid_cols = grid.shape
    piece_rows, piece_cols = piece.shape    
    for i in range(grid_rows - piece_rows + 1):
        for j in range(grid_cols - piece_cols + 1):
            window = grid[i:i + piece_rows, j:j + piece_cols]
            if not np.any(window[piece == 1]):  
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

def test():
    grid = np.array([[1,1,0], [0,0,0], [0,0,0]])
    shapes = [np.array([[1] ])]
    all_sym = generate_all_symmetries(shapes)
    [[print(y) for y in x] for x in generate_translations(grid, all_sym).items()]
    
    grid = np.array([
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ])

    pieces = {
        1: [np.array([
            [1, 1],
            [1, 0],
        ])],
        2: [np.array([[1, 1, 1]])]
    }
    results = generate_translations(grid, pieces)
    print(results)
    

if __name__ == "__main__":
    test()