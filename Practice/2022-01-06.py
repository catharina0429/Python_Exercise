def Digits_mult(number: int) -> int:
    """ Digit multiplication except 0    """
    num = [x for x in list(map(int, str(number).strip("0"))) if x > 0]
    import math
    return math.prod(num)
    ## Clear solution
    # res = 1
    # for d in str(number):
    #     res *= int(d) if int(d) else 1
    # return res

if __name__ == '__main__':
    print('Example:')
    print(Digits_mult(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert Digits_mult(123405) == 120
    assert Digits_mult(999) == 729
    assert Digits_mult(1000) == 1
    assert Digits_mult(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(char.isdigit() for char in password)
    ## Best Clear solution
    # return len(password) > 6 and any(map(str.isdigit, password))

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

def is_acceptable_password3(password: str) -> bool:
    # if password.isdigit() == True:
    #     return False
    # else:
    #     return len(password) > 6 and any(char.isdigit() for char in password)
    return (
        len(password) > 6
            and any(map(str.isdigit, password))
            and not password.isdigit())

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password3("short") == False
    assert is_acceptable_password3("muchlonger") == False
    assert is_acceptable_password3("ashort") == False
    assert is_acceptable_password3("muchlonger5") == True
    assert is_acceptable_password3("sh5") == False
    assert is_acceptable_password3("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

# from typing import List
# def sort_by_ext(files: List[str]) -> List[str]:
#     # return sorted(files, key = lambda x: x.split(".")[-1] if x.split('.')[-2] == '' else x.split('.')[0])
#     # return sorted(files, key = lambda x: (x.split(".")[0], x.split(".")[-1]))
#     # return sorted(files, key = lambda x: (str(x.split(".")[0]), str(x.split(".")[-1])))
#     return sorted(files, key=lambda x: (x.rsplit(".")[0], x.rsplit(".")[-1]))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
#     print("Coding complete? Click 'Check' to earn cool rewards!")
