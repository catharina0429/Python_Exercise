text = 'string'

print('# text의 클래스 확인')
print(text.__class__)

print('\n# text가 str의 인스턴스 오브젝트인지 확인')
print(isinstance(text, str)) # True

print('\n# str 오브젝트의 메소드 확인')
print(text.upper()) # STRING

"""
OOP(Object-Oriented Programming)은 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것
각가의 개체는 메세지를 주고받고, 데이터를 처리할 수 있다.

클래스란 이름의 블루프린트를 이용하여 새로운 데이터 타입을 만들어 
데이터와 함수(클래스 내부에서는 메소드라고 부름)의 논리적 그룹을 만들어 사용하는 것

프로그래밍을 할 때, 2가지 포인트
* 같은 코드를 반복하지 않는다. Don't repeat yourself
* 코드는 항상 바뀔 수 있다는 것을 기억한다.


"""
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

# 인스턴스 변수에 데이터 저장
emp1.first = 'Jane'
emp1.last = 'Doe'
emp1.email = 'Jane.Doe@aaabbb.com'
emp1.pay = 50000

emp2.first = 'John'
emp2.last = 'Doe'
emp2.email = 'John.Doe@aaabbb.com'
emp2.pay = 45000

print('# emp1과 emp2는 다른 메모리 주소값을 가진 별개의 오브젝트입니다.')
print(id(emp1)) # 메모리 주소값 확인
print(id(emp2))
print()

print('# emp1과 emp2는 같은 클래스의 인스턴스인 것을 확인합니다')
class_of_emp1 = emp1.__class__
class_of_emp2 = emp2.__class__
print(id(class_of_emp1))
print(id(class_of_emp2))

# 인스턴스 변수 데이터에 엑세스
print(emp1.email)
print(emp2.email)
# 이렇게 인스턴스 변수를 하나하나 수동으로 할당하면 클래스를 쓰는 의미 없음
# init 메소드를 사용하여 인스턴스를 생성할 때 필요한 데이터를 할당
# __init__ 메소드는 인스턴스가 생성될 때 자동으로 호출되며
# 호출되는 순간 자동으로 인스턴스 오브젝트를 self라는 인자로 받음.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()  + "." + last.lower() + '@aaabbb.com'

    def full_name(self):
        # 매번 print('{}{}'.format(self.first, self.last))로 출력하는 대신
        # class안에 method(function)를 생성해서 호출함
        return '{}{}'.format(self.first, self.last)

emp1 = Employee('Jane', 'Doe', 50000)
emp2 = Employee('John', 'Doe', 45000)

print(emp1.full_name())
print(Employee.full_name(emp1))

