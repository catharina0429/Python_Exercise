## Task 1 Extend the code to mark all duplicate-word errors on a line
import re

s = '''I can see the the red rose and the purple purple lilac.'''

def duplicated_s(string): # find only first duplicates
    try:
        m = re.search(r'\b(\w+)\s+\1\b', string)
        print(string)
        print(' ' * m.start() + '*' * (m.end() - m.start()))
    except:
        print('there is no duplicated')
duplicated_s(s)
duplicated_s('we are doing the assignment')

def find_all_duplicates(string):
    try:
        end_last_word = 0
        m = re.finditer(r'\b(\w+)\s+\1\b', string)
        print(string)
        for i in m:
            no_of_space = i.start() - end_last_word  # end of_last_word - start of the pattern
            no_of_start = i.end() - i.start()  # end - start of the pattern
            print(' ' * no_of_space + '*' * no_of_start, end='')
            end_last_word = i.end()
    except:
        print("please put the proper string!")
find_all_duplicates("I want chocolate")
find_all_duplicates(12345333)
find_all_duplicates(s)

## Task 2 Regex
s2 = '''Ali and Per and friends.\nKari and Joe know each other.\nJames has know Peter since school days.'''
print("Friendsips", '\n', '-' * 20)
for i in s2.split('\n'):
    a = re.findall(r'\b[A-Z].*?\b', i) # [A-Z]+[a-z]+
    a2 = a[0] + ' - ' +  a[1]
    a2 = ' - '.join(a)
    print(a2)

## Task 3 Collecting data via an API
## one plot showing the temperatures at Ås and at Blindern as a function of time
## a scatter plot showing the temperature at Blindern on the y-axis and at Ås on the x-axis
