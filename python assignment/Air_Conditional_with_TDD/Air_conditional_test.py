import unittest
from Air_conditional import *

newAc = Air_conditional()

class AirConditionalTest(unittest.TestCase):
    def test_if_turn_on_exist(self):
        newAc.turn_on()
    
    def test_if_turn_on_changes_the_power_state(self):
        newAc.turn_on()
        self.assertEqual(1, newAc.get_power_state())
    
    def test_if_turn_off_exist(self):
        newAc.turn_off()
    
    def test_if_turn_off_changes_the_power_state(self):
        newAc.turn_off()
        self.assertEqual(0, newAc.get_power_state())
    
    def test_if_increase_temperature_exist(self):
        newAc.increase_temperature(5)
    
    def test_if_increase_temperature_increase_AC_temperature(self):
        newAc.increase_temperature(10)
        self.assertEqual(16, newAc.get_temperature())
    
    def test_if_decrease_temperature_exist(self):
        newAc.decrease_temperature(8)
    
    def test_if_decrease_temperature_decrease_AC_temperature(self):
        newAc.decrease_temperature(8)
        self.assertEqual(16, newAc.get_temperature())
    
    def test_if_temperature_does_not_exceed_30(self):
        newAc.increase_temperature(45)
        self.assertEqual(30, newAc.get_temperature())
    
    def test_if_temperature_do_not_preceed_16(self):
        newAc.decrease_temperature(14)
        self.assertEqual(16, newAc.get_temperature())

if __name__ == "__main__":
    unittest.main()