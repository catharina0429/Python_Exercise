"""
method overriding(무시하다, 우선하다)

기반 클래스의 메서드를 무시하고 새로운 메서드를 만듦.
보통 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때
메서드 오버라이딩을 활용함
원래 기능을 유지하면서 새로운 기눙을 덧붙일 떄
"""

class Person:
    def greeting(self):
        print("Hi")

class Student(Person):
    def greeting(self):
        # Hi라는 단어가 중복되므로 기반 클래스의 메서드를 호출하여 중복을 줄임
        # 기반 클래스의 메서드를 호출하려면 괄호 안에 적어줘야 함
        super().greeting()
        print("I am student")
        # print("Hi, I am student")
        
james = Student()
print(james) # __main__.Student ojbect

james.greeting()

"""
다중 상속(Multi Inheritance): 
여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법

method 탐색 순서(Method Resolution Order;MRO)
클래스.mro()
같은 메서드가 있다면 클래스 목록에서 왼쪽에서 오른쪽 순서로 메서드를 찾음
class D(B, C)인 경우 B가 우선
상속관계가 복잡하게 얽혀 있다면 MRO를 살펴보기
"""

class person_a:
    def greeting(self):
        print("Hi")

class university:
    def manage_credit(self):
        print("credit management")

class undergraduage(person_a, university):
    def study(self):
        print("Study")

jane = undergraduage()
jane.greeting()         # Hi : 기반 클래스 person의 메서드 호출
jane.manage_credit()    # credit management: 기반 클래스 university의 메서드 호출
jane.study()            # study: 파생 클래스 undergraduate에 추가한 study 메서드

print(undergraduage.mro()) # 호출순서는 자기자신, 그 다음이 Person, University
"""
리스트에 기능 추가하기
"""
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
print("previous value: ", x)
x.replace(1, 100)
print("replaced value: ", x)