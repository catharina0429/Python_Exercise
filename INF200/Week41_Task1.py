def letter_freq(text):
    freq = {}
    # 문자열 분리
    # text = text.replace(" ", "")
    s = list(text)
    # 문자열 카운트 후 딕셔너리로 저장
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] = freq[c] + 1
    # 예쁘게 프린트
    for letter, count in sorted(freq.items(), key=lambda x: x[0]):
        print("{:3}{:10}".format(letter, count))

# def letter_freq(text):
#     return {letter: text.count(letter) for letter in set(text)}
# text = "text"
# frequencies = letter_freq(text)
# for letter, count in sorted(freq.items(), key=lambda x: x[0]):
#     print("{:3}{:10}".format(letter, count))

letter_freq("aria is ailen")
