"""
클래스 속성 class property
파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾음
클래스 속성: 모든 인스턴스가 공유됨. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 떄 사용
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

james = Person() # instance
james.put_bag('책')

maria = Person() # instance
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)