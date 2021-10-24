"""
While문 연습해보자
"""
## 1부터 100까지 더하기
# 초기값 지정
num = 0
sum = 0
while num < 100:
    num = num + 1 # num += 1
    sum = sum + num
print(sum)

## 3의 배수의 합
num = 0
sum = 0
while num < 100 :
    num = num + 1 # num += 1
    if num % 3 != 0: continue
    sum = sum + num
print(sum)

## 별 표시하기
num = 0
while num < 4:
    num += 1
    print("*" * num)