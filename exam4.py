'''
__str__() 메서드
<__main__ Address object at 0x0002384D83>

 -> java의 toString()과 유사한 기능
 
'''

class Car :
    def __init__(self, model='sm5', color='black', speed=50) : 
        print('===생성자 호출===')
        self.model = model
        self.color = color
        self.speed = speed
        
    def output(self) :
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)
      
    def __str__(self) :
        print('=== __str__() 호출 ===')
        result = '속도 : ' + str(self.speed) + ', 색상 : ' + self.color
        return result
    
    
myCar = Car()
myCar.output()
print(myCar)
print(myCar.__str__())