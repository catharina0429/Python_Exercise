# from typing import List
# def sort_by_ext(files: List[str]) -> List[str]:
#     # return sorted(files, key = lambda x: x.split(".")[-1] if x.split('.')[-2] != '' else x.split('.')[0])
#     pass
# if __name__ == '__main__':
#     print("Example:")
#     print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
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

def checkio(number: int) -> int:
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
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")