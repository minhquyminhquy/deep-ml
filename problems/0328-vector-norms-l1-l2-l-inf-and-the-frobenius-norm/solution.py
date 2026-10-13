import numpy as np

def compute_l2(arr):
    arr2 = [i * i for i in arr]
    return np.sqrt(np.sum(arr2))

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "linf":
        return float(np.max(np.abs((arr))))

    elif norm_type == "l2":
        if arr.ndim == 2:
            l2_array = []
            for i in range(len(arr)):
                l2_element = compute_l2(arr[i])  
                l2_array.append(l2_element)
            l2_norm = compute_l2(l2_array)
            return float(l2_norm)
        else:
            return float(compute_l2(arr))
    elif norm_type == "l1":
        return float(np.sum(np.abs(arr)))
    else: # frobenisu
        if arr.ndim != 2:
            raise ValueError
        else:
            return float(np.sqrt(np.sum(np.abs(arr) ** 2)))
