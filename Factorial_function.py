def factorial(number: int):
    """
    Return n! (0! is 1)
    :param number: int
    :return: number!
    """
    if number <=1:
        return 1
    result =2
    for n in range(3,number+1):
        result *=n

    return result

for i in range(0,36):
    print(i, factorial(i))
