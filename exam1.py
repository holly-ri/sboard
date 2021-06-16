# 생성자
#   __init__(self)

class Car :
    def __init__(self, model, color, speed) : 
        print('===생성자 호출===')
        self.model = model
        self.color = color
        self.speed = speed
        
        
myCar = Car('k7', 'yellow', 90)
print(myCar.model)
print(myCar.color)
print(myCar.speed)