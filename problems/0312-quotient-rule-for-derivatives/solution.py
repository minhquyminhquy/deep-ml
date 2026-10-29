import numpy as np

def df_x(f_coeffs: list, x:float) -> float:
    if len(f_coeffs) == 1:
        return 0
    elif  len(f_coeffs) == 2:
        return f_coeffs[0]
    df_x = np.sum([i*x**(i-1) * g_coeff for g_coeff, i in zip(f_coeffs[:-2:], range(len(f_coeffs))[:1:-1])])
    df_x += f_coeffs[-2]
    return df_x

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # 2 1 0
    h_x = np.sum([x**i * h_coeff for h_coeff, i in zip(h_coeffs, range(len(h_coeffs))[::-1])])
    g_x = np.sum([x**i * g_coeff for g_coeff, i in zip(g_coeffs, range(len(g_coeffs))[::-1])])
    dh_x = df_x(h_coeffs, x)
    dg_x = df_x(g_coeffs, x)
    return (dg_x*h_x - dh_x*g_x) / h_x**2