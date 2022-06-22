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

    if ((a > b) or (c > a)) and (c > b):
        max = c
    
    if ((b > a) or (a > c)) and (b > c):
        max = b

    if (b > a) or (b > c):
        max = b

    if ((b > a) or (c > b)) and (c > a):
        max = c
    
    if ((a > b) or (b > c)) and (a > c):
        max = a
    
    if (c > a) or (c > b):
        max = c

    if ((c > a) or (b > c)) and (b > a):
        max = b

    if ((a > c) or (c > b)) and (a > b):
        max = a

    return max

print(main(8,-61,7))