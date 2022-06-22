def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """

    answer = 0

    n1 = n % 10
    n //= 10

    n2 = n % 10
    n //= 10

    n3 = n % 10
    n //= 10

    n4 = n % 10
    n //= 10

    n5 = n % 10
    n //= 10

    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        answer += n1

    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        answer += n2

    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        answer += n3

    return answer

print(main(56843))