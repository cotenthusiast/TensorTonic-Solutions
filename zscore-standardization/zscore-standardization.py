import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    return (X - X.mean(axis=axis, keepdims=True)) / np.maximum(eps, X.std(axis=axis, keepdims=True))