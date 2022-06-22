def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = 0
    if (a > b) or (a > c):
        max = a

    if (b > a) or (b > c):
        max = b
    
    if (c > a) or (c > b):
        max = c
        
    return max