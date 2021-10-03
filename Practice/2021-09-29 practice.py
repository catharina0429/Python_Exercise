# Q6
a, b, c = input().split(',')
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)

a, b, c = map(int, input()).split(',')
print(a + b + c)

# Q7
year = 2021
month = '09'
day = 29
hour = 19
minute = 45
second = 30
print(year, month, day, sep = "/")
print(hour, minute, second, sep = ":")

# Q8
test1 = 92
test2 = 40
test3 = 65
test4 = 85
print(test1 >=50 and test2 >= 50 and test3 >= 50 and test4 >= 50)

# Q9
s = '''Python is a programming language that lets you work quickly
and
integrate systems more efficiently.
'''
print(s)

# Q10
a = list(range(5, -10, -2))
a = list(range(1, 10, 2))
print(a)

# Q11
a = [0, 10, 100, 1000]
print(30 in a) # list
print(100 in a)
print(100 not in a)
print(30 in (1, 5, 10, 15)) # tuple
print(1 in range(10))

# print(range(1, 9, 2) + range(2, 10, 2)) # ERROR
print(list(range(1, 11, 2)) + list(range(2, 10, 2)))
print(tuple(range(1, 11, 2)) + tuple(range(2, 10, 2)))

print(a * 3)
print(list(range(1, 5, 2)))
print(tuple(range(2, 6, 2)))

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[-3:] + population[-3:])

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2]) # print odd index

# 12 dictionary = {key: value} 1-1 relation
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'], camille['movement_speed'])

# Q13
x = 5
if x != 10:
    print('ok')

# Q14
if None: # 0, None, '' == False
    print("True")
else :
    print("False")

written_test = 75
coding_test = True
if written_test >= 80 and coding_test == True :
    print('Pass')
else :
    print("Fail")

# Q15 if, else should be used only once, elif can be used multiple times
x = int(input())
if x in range(11, 20): # 11 <= x <= 20
    print('11~20')
elif x in range(21, 30): # 21 <= x <= 30
    print('21~30')
else:
    print("None")

# Q16 # reversed
for i in reversed(range(4)):
    print(i)
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i * 10, end = ' ')

# Q17 while
i = 2
j = 5
while i <= 5 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

# Q18 break continue
i = 0
while True:
    print(i)
    i += 1 # add 1 to i
    if i == 5:
        break

for i in range(10):
    if i % 2 == 0: # divide by 2, mod is equal to 0 -> i is even
        continue
    print(i)

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

i = 0
while i <= 73:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end= ' ')
    i += 1

# Q19
for i in range(2): # two iteration, vertical
    for j in range(4): # 4 iteration, horizontal
        print('*', end = '') # end = '' means no line change
    print()
for i in range(3):
    for j in range(3):
        if j >= i:
            print('*', end = '')
    print()
for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

# Q20
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('dizz')
    else:
        print(i)
for i in range(1, 16):
    print('fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0) or i)