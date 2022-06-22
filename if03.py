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
    if (a > b and a > c) and (b > c):
        answer += b
    
    elif(a > b and a > c) and (b < c):
        answer += c
    
    elif (b > a and b > c) and( a > c):
        answer += a
    
    elif (b > a and b > c) and (a < c):
        answer += c
    
    elif (c > a and c > b) and (a > b) :
        answer += a

    elif (c > a and c > b) and (a < b) :
        answer += b
        
    return answer

print(main(8,-10,-9))