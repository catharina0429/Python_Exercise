## Chapter 23
a = [[10, 20], [20, 30], [30, 40]]
for x, y in a:
    print(x, y)
# way 1
for i in a:
    for j in i:
        print(j, end = ' ')
    print()
# way2
for i in range(len(a)):         # 세로 크기
    for j in range(len(a[i])):  # 가로 크기
        print(a[i][j], end = ' ')
    print()
# way 3
i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1
# way 4
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1
b = [] # create empty list
for i in range(5):
    b.append(i)
print(b)

c = []
for i in range(5):
    line = [] # create empty list for inner list
    for j in range(2):
        line.append(j)
    c.append(line)
print(c)

d = [[0 for j in range(3)] for i in range(2)]
print(d)

e = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(e)

## Q24
print('apple pear grape pineapple orange'.split())
print(' '.join(['apple', 'orange', 'peach', 'pineapple']))
print('python'.upper())
print('PYTHON'.lower())
print('       python      '.rstrip()) # delete white space on the right
print('       python      '.lstrip()) # delete white space on the left
print('       python      '.strip()) # delete white space on both side
print(', python.'.strip(',.').strip())
print('python'.center(30))
print('35'.zfill(4)) # padding 0 with digit

# format specifier
'''%s: string %d: number %f: decimal point default = 6'''
print('%10.2f' % 2.3)
# formating method
'''{index}.format(value)'''
print('hello, {0} {2} {1}'.format('python', 'world', '3.7'))
print('{0:<10}{1:<.1f}'.format('Python', 3.7))

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
def return_filename(string, delimeter):
    splited = string.split(delimeter)
    return splited[-1]
print(return_filename(path, '\\'))

## Q 25
'''dictionary: {key}{value}'''
x = {'a':1, 'b':2, 'c':3}
print(x.items())
print(x.keys())
print(x.values())
for i in x:
    print(i, end = ' ')
for key, value in x.items():
    print(key, value)

score = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(score.values())/len(score)
print(average)

# Q25
# with open('words.txt', 'r') as infile:
#     words = infile.readlines()
#     for word in words:
#         if len(word.strip('\n')) <= 10
#             count += 1
#             print(count)

# Q28
'''Palindrome(회문): 순서를 거꾸로 읽어도 제대로 읽어도 같은 단어와 문장'''
word = input('put your word: ')

is_palindrom = True             # 판별값을 저장할 변수, 초기값은 True
for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 -i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면(python은 0부터 시작)
        is_palindrom = False    # Palindrome이 아님
        break
print(is_palindrom)
# way1
print(word == word[::-1])
# way2
print(list(word) == list(reversed(word)))
# way3
print(word == ''.join(reversed(word)))

## N-gram
text = 'this is python script'
words = text.split()
for i in range(len(words) - 1):
    print(words[i], words[i+1])

n = int(input())
text = input()
words = text.split()
if len(words) < n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)