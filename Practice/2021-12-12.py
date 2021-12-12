# https://py.checkio.org/
def beginning_zeros(number: str) -> int:
    """find how many zero digits ("0") are at the beginning of the given string"""
    initial_value = 0
    for n in number:
        if int(n) == 0:
            initial_value = initial_value + 1
        else:
            return initial_value
    return initial_value

    # Best Answer
    # return len(number) - len(number.lstrip('0'))
if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")

def nearest_value(values: set, one: int) -> int:
    """Find the Nearest Value to the given array"""
    new_dict = {}
    values = list(values)
    values.sort(reverse=True)
    for x in values:
        new_dict.update({abs(one - x): x})
    new_list = sorted(new_dict.keys())
    return new_dict[new_list[0]]
    # Best Answer
    # return min(values, key=lambda n: (abs(one - n), n))

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({0, -2}, -1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({0, -2}, -1) == -2
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

def between_markers(text: str, begin: str, end: str) -> str:
    """returns substring between two given markers"""
    return text[text.find(begin) + 1: text.find(end)]
if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')


def correct_sentence(text: str) -> str:
    """ Returns a corrected sentence which
        starts with a capital letter and ends with a dot(.) """
    if text[-1] != '.':
        return text[0].upper() + text[1:] + '.'
    else:
        return text[0].upper() + text[1:]
if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")

def is_even(num: int) -> bool:
    """Check if the given number is even or not.
       Function should return True if the number is even,
       and False if the number is odd."""
    if num %2 == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")