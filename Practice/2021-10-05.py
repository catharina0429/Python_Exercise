# 38
"""
try:
    실행할 코드
except:
    예외가 발생했을 떄 처리하는 코드
except 예외이름 IndexError, ZeroDivisionError:
    예외가 발생했을 대 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
"""

try:
  x = int(input('put in your number: '))
  y = 10/x
except ZeroDivisionError :
    print("you can not divide by 0")
else:
    print(y)
finally:
    print("execution is done")

try:
    file = open('maria.txt', 'r')
except FileExistsError:
    print("There is no such a file")
else:
    s = file.read()
    file.close()