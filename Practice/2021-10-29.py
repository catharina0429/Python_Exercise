"""
클래스 속성 class property
파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾음
클래스 속성: 모든 인스턴스가 공유됨. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 떄 사용
__init__에서 만든 속성은 인스턴스 속성, self는 현재 인스턴스를 뜻함
"""

class Person:
    bag = []

    def put_bag(self, stuff): # self는 현재 인스턴스를 뜻함
        # self.bag.append(stuff)
        Person.bag.append(stuff) # 클래스 이름으로 클래스 속성에 접근


james = Person() # instance
james.put_bag('책')

maria = Person() # instance
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

print(james.__dict__)
print(Person.__dict__)

class Person:
    def __init__(self): # 인스턴스 속성 사용하기
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person() # instance 속성은 인스턴스별로 독립되어 있으며 서로 영향을 주지 않음
james.put_bag('책')

maria = Person() # instance
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Knight:
    __item_limit = 10 # 비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 안에서만 접근할 수 있음

x = Knight()
x.print_item_limit()  # 10

# print(Knight.__item_limit) # AttributeError 클래스 바깥에서는 접근할 수 없음

class Calc:
    """
    인스턴스를 사용하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드
    static method(정적 메서드): @staticmethod, 매개변수에 self를 지정하지 않음
    매개변수 self가 없으므로 인스턴스 속성에는 접근할 수 없음.
    따라서 보통 정적 메서드는 외부 상태에 영향을 끼치지 않은 pure function을 만들 때 사용
    순수 함수는 side effect가 없고 입력값이 같으면 언제나 같은 출력값을 반환
    """

    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20) # 클래스에서 바로 method 호출
Calc.mul(10, 20) # 클래스에서 바로 method 호출

class person:
    """
    클래스 메서드: 첫 번째 매개변수에 cls(class)를 지정해야 함)
    instance없이 호출할 수 있다는 점에서 static method와 같음
    class method는 class property, class method에 접근해야 할 떄 사용
    """

    count = 0 # class property

    def __init__(self):
        person.count += 1 # person.count = person.count + 1
                          # 인스턴스가 만들어질 때 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명이 생성되었습니다'.format(cls.count)) # cls로 클래스 속성에 접근

sebastian = person()
jorn = person()

person.print_count() # output: 2명이 생성되었습니다

class date:
    """
    날짜 클래스 만들기
    문자열이 올바른 날짜인지 is_date_valid로 확인
    날짜에서 월은 12월까지, 일은 31일까지 있어야 함
    """

    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

if date.is_date_valid('2021-10-31'):
    print('It is a right types of date format.')
else:
    print('It is not right types of date format.')