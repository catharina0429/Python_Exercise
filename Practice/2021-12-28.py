def goes_after(word: str, first: str, second: str) -> bool:
    """to check if one symbol goes only right after another"""
    return True if first in word and second in word and word.find(first) == word.find(second) -1 else False
    ## other solution
    # try:
    #     return word.index(second) - word.index(first) == 1
    # except ValueError:
    #     return False

if __name__ == '__main__':
    print("Example:")
    print(goes_after('almaz', "r","a"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after("almaz","r","a") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

def time_converter(time):
    """to convert the time from the 24-h format into 12-h format"""
    h, m = time.split(":")
    if int(h) == 0:
        return str(int(h) + 12) + ":" + m + " a.m."
    elif int(h) < 12:
        return str(int(h)) + ":" + m + " a.m."
    elif int(h) > 12:
        return str(int(h) - 12) + ":" + m + " p.m."
    else:
        return str(int(h)) + ":" + m + " p.m."
    ## other solution
    # h, m = map(int, time.split(':'))
    # return f"{(h - 1) % 12 + 1}:{m:02d} {'ap'[h > 11]}.m."
    
if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter("00:00") == "12:00 a.m."
    print("Coding complete? Click 'Check' to earn cool rewards!")
