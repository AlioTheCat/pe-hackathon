import numpy as np
from scipy.ndimage import rotate

def generate_symmetries(shape):
    flipped_shape = shape.T

    all_transformations = []
    for angle in [0, 90, 180, 270]:
        rotated = rotate(shape, angle)
        rotated_flipped = rotate(flipped_shape, angle)
        all_transformations.append(rotated)
        all_transformations.append(rotated_flipped)

    unique_transformations = []
    for t in all_transformations:
        if not any(np.array_equal(t, u) for u in unique_transformations):
            unique_transformations.append(t)
            
    return unique_transformations

def generate_all_symmetries(shapes_lst):
    return dict([(i, generate_symmetries(shape)) for i, shape in enumerate(shapes_lst)])
    
def test1():
    shapes = [np.array([[1, 1, 1], [0, 0, 1]]), np.array([[1, 1, 1], [0, 1, 0]])]
    all_sym = generate_all_symmetries(shapes)

    for i, shape_lst in all_sym.items():
        print(f"SHAPE {i}")
        for j, transformation in enumerate(shape_lst):
            print(f"Transformation {j + 1}:\n{transformation}\n")
        print("##################################\n\n")

if __name__ == "__main__":
    test1()