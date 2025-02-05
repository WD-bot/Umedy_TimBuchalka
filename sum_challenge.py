def sum_numbers(*numbers: float)->float:
    """
    Calculates sum of numbers which is passed as arguments
    :param numbers: values
    :return: sum of floats
    """
    result=0
    for number in numbers:
        result += number
    return result

print(sum_numbers(1,2,3))
print(sum_numbers(8,20,2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))


