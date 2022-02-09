# 문자열을 곱해서 여러번 출력가능
from random import random
from tkinter.tix import Tree

# boolean True(O) true(X) / False(O) false(X)
print(True) # -> True
print(False) # -> False
print(not True) # -> False
print(not False) # -> True

name = 'woogie'
age = 29
hobby = 'drinking coffee'
is_adult = age >= 20

print('I like ' + hobby)
# -> I like drinking coffee

# 문자열로 연결하려면 str로 형변환을 해줘야 함
# error message: can only concatenate str (not "int") to str
print('I am ' + name + ', ' + str(age) + ' years old.')
# -> I am woogie, 29 years old.

# 플러스 연산자(+) 대신에 쉼표(,)로 연결할 수도 있는데 이 경우 형변환이 필요없다.
# 쉼표(,)로 연결하면 빈칸이 하나 들어간다.
print('Am I adult?', is_adult)
# -> Am I adult? True


# 동적 타입
age = '스물 아홉'
print('내 나이는', age);

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명: station
변수값: '사당', '신도림', '인천공항' 순서대로 입력
출력문장: xx 행 열차가 들어오고 있습니다.
'''

station = '사당'
print(station, '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station, '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station, '행 열차가 들어오고 있습니다.')

# 제곱 연산자
print(2**3)

# 몫 구하기
print(10//3) # -> 3

# and, or
print(True and False) # -> False
print(True & False) # -> False

print(True or False) # -> True
print(True | False) # -> True

print(random())