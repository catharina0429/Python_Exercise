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
    def print_outputs(*args):  # variable argument
        for arg in args:
            print(arg)
    if a >= 1 and b <= 10000:
        # saved as list
        tmp = [a + b, a - b, a * b, a // b, a % b]
        print_outputs(*tmp) # unpacking
        # print(a + b)
        # print(a - b)
        # print(a * b)
        # print(a // b)
        # print(a % b)
    else:
        print("check your number again")
        return []

print(calc(7, 3))
print(calc(2, 10))

# BJ 10430
"""
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하라.
첫 번째 줄에 A, B, C가 순서대로 주어진다 (2 <= A, B, C <= 10000)
"""
def comp(a, b, c):
    if 2<= a <= 10000 and 2 <= b <= 10000 and 2<= c <= 10000:
        print((a + b) % c )
        print( ((a % c) + (b % c)) % c )
        print( (a * b) % c )
        print( ((a % c) * (b % c)) % c )
    else:
        print("input the right range of number")
print(comp(5, 8, 4))
