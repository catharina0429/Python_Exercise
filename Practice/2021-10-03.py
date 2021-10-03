## 29
def adding(a, b):
    """This function returns a + b"""
    return a + b
print(adding(10, 20))
print(adding.__doc__)

def add_sub(a, b):
    """return two values"""
    return a+b, a-b
x, y = add_sub(10, 20)
print(x, y)
z = add_sub(1, 2)
print(z) # return as tuple

def get_quotient_remainder(a, b):
    return a // b, a % b
quotient, remainder = get_quotient_remainder(10, 3)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

## 30
def print_numbers(*args):
    """variable argument:인수의 개수가 정해지지 않은 가변인수"""
    for i in args:
        print(i)
print_numbers(30, 40, 50)
print_numbers(*[10, 20, 30])

Korean, English, Mathematics, Science = 98, 95, 100, 94
def get_max_score(*args):
    return max(args)
print('Highest Score: ', get_max_score(Science, Mathematics))

## 31
"""Recursion call 
    In python, maximum recursion depth = 1000"""
def hello(count):
    if count == 0: # 반드시 종료조건을 만들어야 함
        return
    print("hello", count)

    count -= 1     # count를 1 감소
    hello(count)   # 다시 hello에 넣음
hello(3)

def factorial(n):
    if n == 1:                # n = 1일 때
        return 1              # 1을 반환하고 recursion call을 끝냄
    return n * factorial(n-1) # n과 factorial 함수에 n-1을 넣어서 반환된 값을 곱함
print(factorial(5))

def is_palindrome(word):
    s = word.lower() # change to lower case
    l = len(s)    # length of word

    if l < 2:     # 종료조건 1: length가 2보다 작으면
        return True
    elif s[0] != s[l-1]: # 종료조건 2: 첫번째 문자와 마지막 문자가 다르면
        return False
    else:
        return is_palindrome(s[1:l-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))
print(is_palindrome('KAYAK'))

## 34 lambda expression
print(lambda x: x + 10)
print((lambda x: x + 10)(2))
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""lambda 매개변수들: 식1 if 조건식1 else 식2
    Note: lambda 표현식에서는 elif 사용할 수 없음"""
print(list(map(lambda x: str(x) if x % 3 == 0 else x, n)))
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, n )))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(list(map(lambda x, y: x * y, a, b)))

def a_filter(x):
    return x % 2 == 0
print(list(filter(a_filter, a))) # filter(함수, 반복가능한 객체): True인 결과값만 반환
print(list(filter(lambda x: x % 2 == 0, a)))

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

