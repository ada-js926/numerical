import numpy as np

def elementwise_operations(array_a, array_b):
    """Perform element-wise multiplication and division."""
    multiplication = np.multiply(array_a, array_b)
    division = np.divide(array_a, array_b)
    return multiplication, division