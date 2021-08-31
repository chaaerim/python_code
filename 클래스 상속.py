class Car:
    def __init__(self, make, model, color, price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price

    def setMake(self, make):
        self.make=make
    def getMake(self):
        return self.make
    def getDesc(self):
        return '차량=('+str(self.make)+','+str(self.model)+','+str(self.color)+','+str(self.price)+')'

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterysize):
        super().__init__(make, model, color, price)
        self.batterysize=batterysize
    def getBattery(self):
        return self.batterysize

myCar=ElectricCar('te', 'model s', 'white', '10000', '100')
myCar.setMake('tesla')
print(myCar.getDesc())
