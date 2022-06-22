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
    answer = 0
    if (a > b) or (a > c):
        answer += a

    if ((a > b) or (c > a)) and (c > b):
        answer += c
    
    if ((b > a) or (a > c)) and (b > c):
        answer += b

    if (b > a) or (b > c):
        answer += b

    if ((b > a) or (c > b)) and (c > a):
        answer += c
    
    if ((a > b) or (b > c)) and (a > c):
        answer += a
    
    if (c > a) or (c > b):
        answer += c

    if ((c > a) or (b > c)) and (b > a):
        answer += b

    if ((a > c) or (c > b)) and (a > b):
        answer += a

    return answer

print(main(8,-61,7))