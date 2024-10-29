import numpy as np
from translation import generate_translations
from symmetries import generate_all_symmetries

grid = np.array([
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1]
])

pieces = {
    1: [np.array([
        [1, 1],
        [1, 0]
    ])],
    2: [np.array([[1, 1, 1]])]
}
results = generate_translations(grid, pieces)
print(results)