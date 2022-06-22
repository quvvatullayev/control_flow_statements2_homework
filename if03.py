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
    if ((a > b and a > c) and (b > c)) or ((c > a and c > b) and (a < b)):
        answer += b
    
    elif((a > b and a > c) and (b < c)) or ((b > a and b > c) and (a < c)):
        answer += c
    
    elif ((b > a and b > c) and( a > c)) or ((c > a and c > b) and (a > b)):
        answer += a
           
    return answer

print(main(88,59,2))