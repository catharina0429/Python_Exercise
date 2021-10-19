# BJ #1008

def div(a, b):
    if a > 0 and b < 10 :
            return a / b
    else:
        print("please input the right number")
        return []

print(div(1, 11))
print(div(1, 3))
print(div(4, 5))

# BJ #10869
"""
두 자연수 A, B가 주어진다. 
이 때, A + B, A - B, A * B, A / B(몫), A % B(나머지)를 출력하는 프로그램을 작성하라.
1<=A, B <=10000
"""
def calc(a, b):
    if a >= 1 and b <= 10000:
        print(a + b)
        print(a - b)
        print(a * b)
        print(a // b)
        print(a % b)
    else:
        print("check your number again")
        return []

print(calc(7,3))