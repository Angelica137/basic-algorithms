def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    It uses a an integer version of the Newton-Raphson algorithm

    Time complexity:
        O(log n) as we halve teh number of iterations each
        time we go through the while loop
    """
    if number < 0:
        raise ValueError("Cannot compute square root of negative number")
    if number == 0 or number == 1:
        return number

    x = number
    y = (x + number // x) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2
    return x


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
