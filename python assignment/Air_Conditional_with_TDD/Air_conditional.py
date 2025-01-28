class Air_conditional:
    _power_state = 0
    _temperature = 16

    def turn_on(self):
        self.set_powerstate(1)

    def turn_off(self):
        self.set_powerstate(0)
    
    def get_power_state(self):
        return self._power_state
    
    def increase_temperature(self, temperature_value:int):
        self.check_temperature_value(temperature_value)
        # self.set_temperature(temperature_value)
    
    def set_temperature(self, temperature_value:int):
        self.temperature = temperature_value

    def set_powerstate(self, state:int):
        self._power_state = state
    
    def get_temperature(self):
        return self.temperature
    
    def decrease_temperature(self, temperature_value:int):
        # self.set_temperature(temperature_value)
        self.check_temperature_value(temperature_value)
    
    def check_temperature_value(self, temperature_value:int):
        if type(temperature_value) in [int, float]:
            if(self.is_temperature_greater_than_30(temperature_value)):
                self.set_temperature(30)
                return
            elif (self.is_temperature_less_than_16(temperature_value)):
                self.set_temperature(16)
                return
            else:
                self.set_temperature(temperature_value)
                return
        raise ValueError
    
    def is_temperature_greater_than_30(self, temperature_value):
        if temperature_value > 30:
            return True
        return False
    
    def is_temperature_less_than_16(self, temperature_value):
        if temperature_value < 16:
            return True
        return False
    
