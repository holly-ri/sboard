'''
파이썬은 기본적으로 public으로 설정되어 있다
private
  __name
'''
class Car :
    def __init__(self, model='sm5', color='black', speed=50, maker='삼성') : 
        print('===생성자 호출===')
        self.model = model
        self.color = color
        self.speed = speed
        self.__maker = maker
        
    def output(self) :
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)
        print('회사 :', self.__maker)
        
    def getMaker(self) :
        return self.__maker
    
    def setMaker(self, maker) :
        self.__maker = maker
        
myCar = Car()
myCar.output()
print('-' * 20)

print(myCar.model)
print('-' * 20)

myCar.setMaker('현대')
myCar.output()
print('-' * 20)

print(myCar.getMaker())