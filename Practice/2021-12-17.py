def bigger_price(limit: int, data: list) -> list:
    """ TOP most expensive goods """
    sorted_data = sorted(data, key = lambda item: (-item['price']))
#     sorted_data = sorted(data, key = lambda item: item['price'], reverse = True)
    return sorted_data[:limit]
if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')

def between_markers(text: str, begin: str, end: str) -> str:
    """ Returns substring between two given markers """
    start = text.find(begin) + len(begin) if text.find(begin) != -1 else 0
    end = text.find(end) if text.find(end) != -1 else len(text)
    return text[start:end] if start < end else ''

if __name__ == '__main__':
    print('Example:')
    print(between_markers('No hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

def checkio(data: list) -> list:
    """Non-unique Elements"""
    # set([x for x in a if a.count(x) > 1]) # unique
    d2 = []
    for i in data:
        if data.count(i) >= 2:
            d2.append(i)
    return d2

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

def popular_words(text: str, words: list) -> dict:
    """Popular Words"""
    text2 = text.lower().split()
    new_list = {}
    for word in words:
        try:
            new_list[word] = text2.count(word)
        except:
            new_list[word] = 0
    return new_list
if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
