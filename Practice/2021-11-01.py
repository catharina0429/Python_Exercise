
class Employee:
    raise_amount = 1.1 # 1 연봉인상률 클래스 변수

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@aaabbb.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}"입니다.'.format(self.full_name(), self.pay)

    # 1 클래스 메소드 데코레이터를 사용하여 클래스 메소드 정의
    @classmethod
    def change_raise_amount(cls, amount):
        # 2 인상률이 1보다 작으면 재입력 요청
        while amount < 1:
            print('[Warning] 인상율은 1보다 작을 수 없습니다')
            amount = input('[Input] Please input the right rise amount: ')
            amount = float(amount)

        cls.raise_amount = amount
        print('인상울 "{}"가 적용되었습니다.'.format(amount))

emp1 = Employee('Jane', 'Doe', 70000)
print(emp1.get_pay()) # 연봉 인상 전
emp1.apply_raise() # 연봉 인상 적용
print(emp1.get_pay()) # 연봉 인상 후

emp2 = Employee('John', 'Doe', 60000)
print(emp2.get_pay()) # 연봉 인상 전
Employee.change_raise_amount(0.8) # 연봉인상율 변경
print(emp2.get_pay()) # 연봉 인상 후
