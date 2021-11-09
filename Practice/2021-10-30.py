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