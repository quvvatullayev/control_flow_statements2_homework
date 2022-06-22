def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """

    answer = 0
    if a > b and a > b and b > c:
        answer += b
    
    elif b > a and b > c and a > c:
        answer += a
    
    else:
        answer += c
        
    return answer

print(main(8,6,9))