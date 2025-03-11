class Bike:
    powerState = 0
    speed = 0
    gear = 0

    def turnOn(self):
        self.setPowerState(1)
    
    def setPowerState(self, state:int):
        self.powerState = state
    
    def turnOff(self):
        self.setPowerState(0)
    
    def accelerate(self, currentGear:int):
        self.speed += currentGear

    def decelerate(self, currentGear:int):
        self.speed -= currentGear

    def setGear(self, value:int):
        self.gear = value
    
    def selectGearAutomatically(self, speed:int):
        
        if self.gearForSpeedRange0_20(speed):
            self.setGear(1)
        elif self.gearForSpeedRange21_30(speed):
            self.setGear(2)
        elif self.gearForSpeedRange31_40(speed):
            self.setGear(3)
        elif self.gearForSpeedRange41_above(speed):
            self.setGear(4)

            
    
    def gearForSpeedRange0_20(self, speed:int):
        return speed in [range(0, 21)]
    
    @staticmethod
    def gearForSpeedRange21_30(speed:int):
        return speed in [range(21, 31)]
    
    def gearForSpeedRange31_40(self, speed:int):
        return speed in [range(31, 41)]
    
    def gearForSpeedRange41_above(self, speed:int):
        return speed in [range(41, 200)]
