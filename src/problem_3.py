def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums

    This algorithm uses the Counting sort algorithm to count occurences of digits
    and help sort th input array

    Time complexity:
        O(n) where n is the length of count no more than 10
    """
    # Create a list of 10 items all 0 to count how many times a number appears
    count = [0] * 10
    for num in input_list:
        count[num] += 1

    # Create two numbers
    num1, num2 = 0, 0
    toggle = 0  # 0 for num1, 1 for num2

    # Iterate from 9 to 0 (largest to smallest digit)
    for i in range(9, -1, -1):
        while count[i] > 0:
            if toggle == 0:
                num1 = (
                    num1 * 10 + i
                )  # need mult by 10 to move prev digit to correct position
                toggle = 1
            else:
                num2 = num2 * 10 + i
                toggle = 0
            count[i] -= 1

    return [num1, num2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
