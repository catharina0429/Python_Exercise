def translate(text: str) -> str:
    """Bird Language"""
    import re
    # vowels = "aeiouy"
    # re.findall('[a|e|i|o|u|y]+', text)
    return re.sub(r'([aeiouy])\1\1|([a-z])[aeiouy]', r'\1\2', text, flags=re.I)

if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")

def checkio(line1: str, line2: str) -> str:
    """Common Words"""
    l1 = line1.split(",")
    l2 = line2.split(",")
    line = sorted([value for value in l1 if value in l2], key = str.lower)
    return ",".join(line)

    ## Clear solution
#     first_set, second_set = set(line1.split(",")), set(line2.split(","))
#     common = first_set.intersection(second_set)
#     return ",".join(sorted(common))
if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
