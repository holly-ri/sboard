'''
random함수 사용
'''

from random import random
from random import randint
from random import randrange
from random import sample

# random()  0~1의 임의의 실수 1개 생성
print(random())

# randint(start, end) : start~end까지 정수를 1개 생성 
print(randint(0, 9))   # end 숫자도 포함
print('-' * 20)

# randrange(start, end, step) : start~end까지 step을 줄수있다
print(randrange(5, 10))    
print(randrange(5, 10, 2))  # 5, 7, 9 중에서 1개 생성

# 임의의 문자 생성 : 아스키코드  A(65)  a(97)
print(chr(randint(65, 90)))
print(chr(randint(97, 122)))

# sample : 리스트목록 중에서 한개 추출
print(sample([1,2,3,4,5,6,7,8,9], 6))
print(sample([a for a in range(1, 46)], 6))