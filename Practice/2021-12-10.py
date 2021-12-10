def end_zeros(num: int) -> int:
    """Try to find out how many zeros a given number has at the end"""
    return len(str(num)) - len(str(num).rstrip('0'))
if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

def backward_string(val:str) -> str:
    """return a given string in reverse order"""
    return val[::-1]
if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")

from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    """Remove from the list all of the elements before the given one"""
    # your code here
    if border in items:
        i = items.index(border)
        return items[i:]
    else:
        return items
if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")

def is_all_upper(text:str) -> bool:
    """Check if a given string has all symbols in upper case"""
    for char in text:
        if char.islower():
            return False
    return True
if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('mixed UPPER and lower'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

def replace_first(items: list) -> Iterable:
    """In a given list the first element should become the last one"""
    if len(items) <= 1:
        return items
    else:
        tmp = items[1:]
        tmp.append(items[0])
        return tmp
if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

def max_digit(number: int) -> int:
    """determine which digit in the given number is the biggest"""
    return int(max(str(number)))
if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

def split_pairs(a):
    """Split the string into pairs of two characters"""
    if len(a) %2 != 0:
        tmp = a + str('_')
        return [tmp[i:i+2] for i in range(0, len(tmp), 2)]
    else:
        return [a[i:i+2] for i in range(0, len(a), 2)]
if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

def beginning_zeros(number: str) -> int:
    # your code here
    return 0
