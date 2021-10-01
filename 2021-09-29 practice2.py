# Ch. 22
'''리스트는 method(object에 속한 함수를 뜻함)를 제공함.
대표적으로 append, extend, insert, remove가 있음'''
a = [38, 21, 53, 62, 19]
# way 1
for index, value in enumerate(a, start = 1):
    print(index, value)
# way 2
for i in range(len(a)):
    print(a[i])
# way 3
i = 0
while i < len(a):
    print(a[i])
    i += 1

'''find smallest number'''
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print("smallest: ", smallest)

x = [i for i in range(10)]
y = list(i for i in range(10))
print(x == y)

z = [i for i in range(10) if i % 2 == 0]
print(z)

w = [i ** j for j in range(1, 4)
            for i in range(1, 4)]
print(w)

'''list(map(function, list))'''
u = [1.3, 2.5, 4.6, 7.8]
for i in range(len(u)):
    u[i] = int(u[i])
print(u)

u2 = list(map(int, u))
print(u2)

'''Tuple: immutable'''
t = (29, 10, 3, 15, 50)
for i in t:
    print(i, end = ' ')

# Chapter 22 Practice
c = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
d = [i for i in c if len(i) == 5]
print(d)