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
        
myCar = Car()
myCar.output()
print('-' * 20)

myCar1 = Car('k5')
myCar1.output()
print('-' * 20)

myCar2 = Car(color='blue')
myCar2.output()
print('-' * 20)

myCar3 = Car(speed=100)
myCar3.output()
print('-' * 20)

myCar4 = Car('sonata', 'red', 80)
myCar4.output()
print('-' * 20)

myCar5 = Car(speed=80, model='sonata', color='red')
myCar5.output()
print('-' * 20)

myCar6 = Car('sonata2', 'blue', 60)
myCar6.output()
print('-' * 20)

myCar6.__init__('sonata3', 'yellow', 40)
myCar6.output()