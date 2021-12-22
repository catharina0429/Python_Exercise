def second_index(text: str, symbol: str) -> [int, None]:
    """ Returns the second index of a symbol in a given text"""
    import re
    try:
        tmp = list(re.finditer(symbol, text))
        if len(tmp) >=2:
            return tmp[1].start()
    except:
        return None
    ## Best answer
    # try:
    #     return text.index(symbol, text.index(symbol) +1)
    # except:
    #     return None
if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

def frequency_sort(items):
    """Sort array by element frequency"""
    # try:
    #     if len(items) == 0:
    #         return []
    #     for i in items:
    #         if items.count(i) > 1:
    #             tmp = sorted(items, reverse = True)
    #             return sorted(tmp, key = tmp.count, reverse = True)
    #         else:
    #             return items
    # except:
    #     return []
    return sorted(items, key = lambda x: (-items.count(x), items.index(x)))

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([1,2,2,1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
