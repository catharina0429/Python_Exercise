"""
Class inheritance(클래스 상속)물려받은 기능을 유지한 채로 다른 기능을 추가할 때 사용
Base class(기반 클래스; parent or super-class) -> Derived class(파생 클래스; child or sub-clss)
클
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
