def is_square(n):
    """
    Performs Newton's Method (n + 1)/2:
    Looks for the largest integer x for which x*x does not exceed n.
    Checks if highest value is equal to input.
    If yes, then True. If not, then False.
    """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    
    # False for negative cases
    if n < 0:
        return False
    # True for zero case
    elif n == 0:
        return True
    # True for test case
    elif x*x == n:
        return True
    # Otherwise False
    else:
        return False
