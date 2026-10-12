import numpy as np

def statistical_calculations(arr):
    """Calculate mean, median, and standard deviation."""
    mean_val = np.mean(arr)
    median_val = np.median(arr)
    std_val = np.std(arr)
    return mean_val, median_val, std_val