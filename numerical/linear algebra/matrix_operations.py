import numpy as np

def matrix_add_subtract(matrix_a, matrix_b):
    """Perform matrix addition and subtraction."""
    addition = np.add(matrix_a, matrix_b)
    subtraction = np.subtract(matrix_a, matrix_b)
    return addition, subtraction