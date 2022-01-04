def most_frequent(data: list) -> str:
    """ Determines the most frequently occurring string in the sequence. """
    # [[x, data.count(x)] for x in set(data)].max
    return max(data, key = data.count)

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")

def easy_unpack(elements: tuple) -> tuple:
    """ Returns a tuple with 3 elements - first, third and second to the last """
    return (elements[0], elements[2], elements[-2])

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

def words_order(text: str, words: list) -> bool:
    # your code here
    # list(set(text.split(" ")).intersection(words))
    # return [x for x in text.split(" ") if x in words] == words
    # return [x for x in list(set(text.split(" "))) if x in words] == words

if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    assert words_order("hi world world im here",["world","world"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
