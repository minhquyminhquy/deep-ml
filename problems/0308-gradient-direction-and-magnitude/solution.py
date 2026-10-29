import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    grad_arr = np.asarray(gradient, dtype=float)
    magnitude = float(np.linalg.norm(grad_arr))
    
    # Avoid division by zero when magnitude is 0
    if magnitude == 0:
        direction = np.zeros_like(grad_arr)
    else:
        direction = grad_arr / magnitude
        
    descent_direction = -direction
    
    return {
        'magnitude': magnitude, 
        'direction': direction.tolist(),
        'descent_direction': descent_direction.tolist()
    }