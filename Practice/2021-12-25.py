MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "space": " "
}
def morse_decoder(code):
    """ Morse Decoder """
    code = code.replace("   ", " space ").split()
    tmp = []
    for char in code:
        tmp.append(MORSE[char])
    return "".join(tmp).capitalize()

if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- ..."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert (
        morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
        == "It was a good day"
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")

def safe_pawns(pawns: set) -> int:
    """Pawn Brotherhood"""
    p = {(ord("8") - ord(x[1]),
          ord(x[0]) - ord("a")) for x in pawns}
    s1 = {(x[0] - 1, x[1] - 1) for x in p}
    s2 = {(x[0] - 1, x[1] + 1) for x in p}
    return len(p & s1 | p & s2)
    ## Speedy solution
    # return sum((any(chr(ord(l) + i) + str(int(d) - 1) in pawns
    #                 for i in [-1, 1])) for l, d in pawns)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

def checkio(values: list) -> list:
    """Absolute Sorting"""
    return sorted(values, key = abs)

if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")


def checkio(in_string):
    """Remove accents"""
    import unicodedata
    nfkd_form = unicodedata.normalize('NFKD', in_string)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
