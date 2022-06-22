def main(a,b,c):
    answer = 0
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (b > a and a > c) or (b < a and a < c):
        answer += a
    
    elif (a > b and b > c) or (a < b and  b < c):
        answer += b
    
    else:
        answer += c
           
    return answer
print(main(88,59,200))