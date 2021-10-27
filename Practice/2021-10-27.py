"""
closure(클로저)
어떤 함수를 함수 자신이 가지고 있는 환경과 함께 저장한 레코드
함수가 가진 free variable을 클로저가 만들어지는 당시의 값과 레퍼런스에 매핑해 주는 역할
일반함수와 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한뒤
이 캡퍼한 값들에 액세스 할 수 있게 도와준다.

free variable(프리변수)
코드 블럭 안에서 사용되었지만, 그 코드 블럭 안에서 정의되지 않은 변수
"""

def outer_func():       #1
    message = 'Hi'      #3 message라는 변수에 'Hi'라는 문자열 할당

    def inner_func():   #4 inner func을 정의하고
        print(message)  #6 호출과 동시에

    # return inner_func() #5 값을 반환한다
    return inner_func   #5 ()를 지울 경우, 아무것도 출력 안됨

# outer_func()            #2: #1에서 정의된 함수를 #2에서 출력함
my_func = outer_func()    #2: 반환값인 inner_func를 변수에 할당함 출력은 안함

print(my_func)            #7: my_func에 inner_func함수 오브젝트가 할당되어 있음
print()
print(dir(my_func))       #8: __closuer__라는 속성에 데이터를 숨김
print()
print(type(my_func.__closure__))  #9: 클로저는 튜플!
print()
print(my_func.__closure__)  #10: 튜플 안에 뭐가 있는 지 확인
print()
print(my_func.__closure__[0])  #11: 튜플의 첫번째 아이템은 cell이라는 문자열 오브젝트
print()
print(dir(my_func.__closure__[0]))  #12: 오브젝트 안에 여러 속성들이 있음
print()
print(my_func.__closure__[0].cell_contents)  #13: cell_contents에는 Hi가 들어있음

def outer_func(tag):   #1
    text = 'Some text' #5
    tag = tag          #6

    def inner_func(text):   #7
        print('<{0}>{1}<{0}>'.format(tag, text)) #9

    return inner_func       #8

h1_func = outer_func('h1')  #2
p_func = outer_func('p')    #3

h1_func('h1 태그의 안쪽')     #4
p_func('p 태그의 안')         #10

def calc():
    a = 3
    b = 5
    def mul_add(x):
        # return a*x + b # 함수 바깥쪽에 있는 지역변수 , a, b를 사용하여 게산
        return lambda x: a * x + b #람다표현식을 반환함
    return mul_add

c = calc()
print(c(1), c(2), c(3))