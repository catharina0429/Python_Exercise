from typing import Union
def sun_angle(time: str) -> Union[int, str]:
    """Sun angle"""
    h, m = time.split(":")
    mm = (int(h) - 6) * 60 + int(m)
    return (round(mm/720 *180, 2) if mm <= 720 and mm >= 0 else "I don't see the sun!")

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

def split_list(items: list) -> list:
    """Split List"""
    if len(items) == 0:
        return [[], []]
    elif len(items) == 1:
        return [items, []]
    else:
        l = len(items) /2
        if len(items) %2 == 0:
            return [items[:int(l)], items[int(l):]]
        else:
            return [items[:int(l)+1], items[-int(l):]]
    ## Other solutions
    # s = (len(items) + 1) // 2
    # return [items[:s], items[s:]]

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
