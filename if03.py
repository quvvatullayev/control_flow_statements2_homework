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
    if (b > a and a > c) or (b < a and c > a):
        answer += a
    
    elif (b > c and c > a) or (b < c and a > c):
        answer += c
    
    else:
        answer += b
           
    return answer

print(main(88,59,2))