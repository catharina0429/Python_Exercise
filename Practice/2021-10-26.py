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
        result.append(func(i)) # call square function, func == square
    return  result

numeric_list = [1, 2, 3, 4, 5]

square = my_map(square, numeric_list)
print(square)

