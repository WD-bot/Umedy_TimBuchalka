def is_palindrome(string: str)->bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards as backwards.
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards=string[::-1]
    # return backwards == string #TRUE or False
    return string[::-1].casefold()==string.casefold() # [::-1] makes it backwards
    # == is to see if its TRUE or False


def palindrome_sentence(sentence: str)-> bool:
    """
    Check if a sentence is a palindrome.
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string= ""
    for char in sentence:
        if char.isalnum(): # The isalnum() method returns True if all characters in the string are alphanumeric
            string+=char
    print(string)
    # return string[::-1].casefold()==string.casefold()
    return is_palindrome(string)


word = input("Please enter a word or sentence to check if it's a palindrome:")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

p= palindrome_sentence()