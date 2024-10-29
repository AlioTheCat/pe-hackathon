import numpy as np

def translation_2(grid, pieces):
    valid_positions = {}
    grid_rows, grid_cols = grid.shape

    for piece_num, piece in pieces.items():
        piece_rows, piece_cols = piece.shape
        valid_positions[piece_num] = []
        piece_mask = (piece == 1)
        for i in range(grid_rows - piece_rows + 1):
            for j in range(grid_cols - piece_cols + 1):
                window = grid[i:i + piece_rows, j:j + piece_cols]
                if np.all((window[piece_mask] == 0)):  
                    new_grid = np.copy(grid)
                    new_grid[i:i + piece_rows, j:j + piece_cols] += piece
                    valid_positions[piece_num].append(new_grid)

    return valid_positions