def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    def derivative(a, b, x):
        return 2*a*x + b
    
    while steps >= 0:
        grad = derivative(a, b, x0)
        x0 -= lr * grad
        steps -= 1

    return x0