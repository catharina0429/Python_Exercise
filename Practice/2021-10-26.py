"""
파이썬 - 퍼스트 클래스 함수(First class function)
함수 자체를 인자(argument)로써 다른 함수에 전달하거나,
다른 함수의 결과값으로 리턴할 수 도 있고
함수를 변수에 할당하거나 데이터 구조 안에 저장할 수 있는 함수를 뜻함
"""
def square(x):
    return x * x
print(square(5))

f = square # f라는 변수에 square라는 함수를 할당

print(square) # 둘 다 메모리 주소값이 동일함
print(f)      #
print(f(5))   # 할당된 변수도 함수처럼 사용할 수 있음

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i)) # call(호출) square function, func == square
    return  result

numeric_list = [1, 2, 3, 4, 5]

square = my_map(square, numeric_list)
print(square)

# 간단한 함수 하나만을 실행할 때는 아래처럼 일반 함수를 사용할 수 있음
# First class function을 사용하는 이유는 이미 정의된 여러 함수를 간단히 재활용 할 수 있기 때문
def simple_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i * i)
    return result

simple_square_res = simple_square(numeric_list)
print(simple_square_res)

def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def added_my_map(func, arg_list):
    # wrapper 한수 하나만 정의해서 기존의 함수나 모듈을 사용할 수 있음
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares_res = added_my_map(square, numeric_list)
cubes_res = added_my_map(cube,numeric_list)
quads_res = added_my_map(quad, numeric_list)

print(squares_res)
print(cubes_res)
print(quads_res)

# Example 2
def logger(msg):
    def log_message(): # closuer 클로저: 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억함
        print('Log: ', msg)
    return log_message

log_hi = logger("Hi")
print(log_hi) # log_message의 오브젝트가 출력됨
log_hi() # "Log: Hi"가 출력됨

del logger # global namespace에서 logger 오브젝트를 지움

# logger 오브젝트가 지워진 것을 확인
try:
    print(logger)
except NameError:
    print('NameError: logger는 존재하지 않습니다.')

log_hi() # logger가 지워진 뒤에도 log: Hi는 출력됨




