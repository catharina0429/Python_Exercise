"""
Class inheritance(클래스 상속)물려받은 기능을 유지한 채로 다른 기능을 추가할 때 사용
Base class(기반 클래스; parent or super-class) -> Derived class(파생 클래스; child or sub-clss)
클
상속은 같은 종류이면서 동등한 기능일 때 사용한다는 점이 중요
"""

class person:
    def greeting(self):
        print("Hello")

class student(person):
    def study(self):
        print("Study Python")

hedda = student()
hedda.greeting() #output: Hello ; base class인 person의 메서드 호출
hedda.study() #output: Study Python ; derived class인 student의 메서드 호출

issubclass(student, person) #output: True; student가 person의 파생클래스인지 확인할 뗴

"""
포함관계: has-a relation
같은 종류에 동등한 관계일 때는 inheritance를 사용하고
그 외에는 속성에 instance를 넣는 포함 방식을 사용하면 됨
"""
class Person:
    def greeting(self):
        print("Hello")

class PersonList:
    def __init__(self):
        self.person_list = [] # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person): # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

"""
method overriding
원래 기능은 유지하면서 새로운 기능을 덧붙일 떄
중복되는 기능은 파생클래스에서 다시 만들지 않고, 기반클래스의 기능을 사용
"""
class Person:
    def greeting(self):
        print("Hello")

class Student(Person):
    def greeting(self):
        super().greeting() # base class(여기선 Person)의 method를 호출하여 중복을 줄임
        print('I am studing Python')

taylor = Student()
taylor.greeting()

"""
multi inheritance(다중상속):
여러 base class로부터 상속을 받아서 derive class를 만드는 방법

method 탐색 순서(Method Resolution Order;MRO)
같은 메서드가 있다면 클래스 목록에서 왼쪽에서 오른쪽 순서로 메서드를 찾음
class D(B, C)인 경우 B가 우선
"""

class Person:
    def greeting(self):
        print("Hi")

class University:
    def manage_credit(self):
        print("manage credit")

class bacheolor(Person, University):
    def study(self):
        print("Study hard, enjoy much")

jane = bacheolor()
jane.greeting()      #ouput: Hi; Base class(Person)의 method 호출
jane.manage_credit() #output: manage credit; Base Class(University)의 method 호출
jane.study()         #output: Study hard, enjoy much; Derived class(bacheolor)에 추가한 study method

print(bacheolor.mro()) # 호출순서는 자기자신, 그 다음이 Person, University

"""
abstract class(추상 클래스)
"""