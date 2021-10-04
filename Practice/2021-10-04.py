# 33
"""
    global variable: 스크립트 전체에서 접근할 수 있는 변수
    global scope: global variable에 접근할 수 있는 범위
    local variable: 함수 내에서 생성된 변수 함수 밖에선 호출 안됨
    local scope: local variable이 접근할 수 있는 범위
"""
x = 10        # global variable
def foo():
    global x  # global variable x를 사용하겠다고 설정
              # global variable이 없을 때 함수 내부에 설정해주면 global variable이 된다
    x = 30
    print(x)  # print local variable
foo()
print(x)      # print global variable

def foo():
    x = 20    # x는 foo의 지역변수
    print(x)
foo()         # local variable 출력
print(x)      # global variable 출력

def A():
    x = 10 # A의 지역변수
    y = 100
    def B():
        nonlocal x # 현재 함수의 바깥쪽에 있는 지역변수 사용
        """nonlocal은 현재함수 바깥쪽에 있는 지역변수를 찾을 때 
           가장 가까운 함수부터 먼저 찾음"""
        x = 20 # A의 지역변수 x에 20 할당(지역변수 값 변경)
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
    print(x) # A의 지역변수 출력
A() # nonlocal x를 설정하면 20, 안 하면 10이 출력됨

def calc():
    """
    Closure: 함수를 둘러싼 환경(지역변수, 코드 등)을 계속 유지하다가 함수를 호출할 때 다시 꺼내서 사용하는 함수
    """
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b # 함수 바깥쪽에 있는 local variable a, b를 사용해서 계산
    return mul_add       # mul_add 함수를 반환
c = calc()
print(c(1), c(2), c(3), c(4))

def calc():
    a = 3
    b = 5
    """lambda expression: anonymous function
       closer: 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수"""
    return lambda x: a * x + b # lambda 표현식을 반환
c = calc()
print(c(1), c(2), c(3), c(4))

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)

def counter():
    i = 0            # 지역변수 할당
    def count():
        nonlocal i   # 현재 함수의 바깥쪽에 있는 지역변수 사용
        i += 1
        return i
    return  count    # 함수를 반환할 때는 함수 이름만 반환 ()붙이면 안됨
c = counter()
for i in range(10):
    print(c(), end = ' ')
