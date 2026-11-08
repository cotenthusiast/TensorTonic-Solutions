import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.array(y)

    matrix = np.zeros((len(y), num_classes if num_classes is not None else max(y) + 1))

    matrix[np.arange(len(y)), y] = 1

    return matrix