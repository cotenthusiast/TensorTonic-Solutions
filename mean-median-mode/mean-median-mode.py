from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    return {
        "mean": float(x.mean()),
        "median": float(np.median(x)),
        "mode": float(np.unique(x, return_counts=True)[0][np.argmax(np.unique(x, return_counts=True)[1])])
    }