import random
import unittest
import Bike

newBike = Bike.Bike()
class Bike_test(unittest.TestCase):

    def test_if_turn_on_function_exit(self):
        newBike.turnOn()
    
    def test_if_turn_on_function_turns_bike_on(self):
        newBike.turnOn()
        self.assertEqual(1, newBike.powerState)
    
    def test_if_turn_off_function_exist(self):
        newBike.turnOff()
    
    def test_if_turn_off_function_turns_bike_off(self):
        newBike.turnOff()
        self.assertEqual(0, newBike.powerState)
    
    def test_if_accelerate_function_exist(self):
        newBike.accelerate(newBike.gear)

    def test_if_accelerate_function_increases_speed_by_1_for_gear_1(self):
        initial_speed = newBike.speed
        n = 1
        newBike.setGear(n)
        newBike.accelerate(n)
        self.assertEqual(initial_speed + n, newBike.speed)
    
    def test_if_accelerate_function_increases_speed_by_2_for_gear_2(self):
        initial_speed = newBike.speed
        n = 2
        newBike.setGear(n)
        newBike.accelerate(n)
        self.assertEqual(initial_speed + n, newBike.speed)
    
    def test_if_accelerate_function_increases_speed_by_3_for_gear_3(self):
        initial_speed = newBike.speed
        n = 3
        newBike.setGear(n)
        newBike.accelerate(n)
        self.assertEqual(initial_speed + n, newBike.speed)

    def test_if_accelerate_function_increases_speed_by_4_for_gear_4(self):
        initial_speed = newBike.speed
        n = 4
        newBike.setGear(n)
        newBike.accelerate(n)
        self.assertEqual(initial_speed + n, newBike.speed)

    def test_if_decelerate_function_exist(self):
        newBike.decelerate(newBike.gear)
    
    def test_if_decelerate_function_decreases_speed_by_1_for_gear_1(self):
        initial_speed = newBike.speed
        n = 1
        newBike.setGear(n)
        newBike.decelerate(n)
        self.assertEqual(initial_speed -n, newBike.speed)

    def test_if_decelerate_function_decreases_speed_by_2_for_gear_2(self):
        initial_speed = newBike.speed
        n = 2
        newBike.setGear(n)
        newBike.decelerate(n)
        self.assertEqual(initial_speed -n, newBike.speed)

    def test_if_decelerate_function_decreases_speed_by_3_for_gear3(self):
        initial_speed = newBike.speed
        n = 3
        newBike.setGear(n)
        newBike.decelerate(n)
        self.assertEqual(initial_speed -n, newBike.speed)

    def test_if_decelerate_function_decreases_speed_by_4_for_gear_4(self):
        initial_speed = newBike.speed
        n = 1
        newBike.setGear(n)
        newBike.decelerate(n)
        self.assertEqual(initial_speed -n, newBike.speed)

    def test_if_gear_follows_correct_range_for_speed_0_20(self):
        """
        Gear 1: 0 - 20
        b)Gear 2: 21 - 30 c) Gear 3: 31 - 40 d) Gear 4: 41 and above
        These gear changes automatically as soon as the bike gets exceeds any of these speed
        ranges either through acceleration or deceleration.
        """
        speed = list(range(0, 21))
        newBike.selectGearAutomatically(random.choice(speed))
        self.assertEqual(1, newBike.gear)


    def test_if_gear_follows_correct_range_for_speed_21_30(self):
        """
        Gear 1: 0 - 20
        b)Gear 2: 21 - 30 c) Gear 3: 31 - 40 d) Gear 4: 41 and above
        These gear changes automatically as soon as the bike gets exceeds any of these speed
        ranges either through acceleration or deceleration.
        """
        speed = list(range(21, 31))
        newBike.selectGearAutomatically(random.choice(speed))
        self.assertEqual(2, newBike.gear)

    def test_if_gear_follows_correct_range_for_speed_31_40(self):
        """
        Gear 1: 0 - 20
        b)Gear 2: 21 - 30 c) Gear 3: 31 - 40 d) Gear 4: 41 and above
        These gear changes automatically as soon as the bike gets exceeds any of these speed
        ranges either through acceleration or deceleration.
        """
        speed = list(range(31, 40))
        newBike.selectGearAutomatically(random.choice(speed))
        self.assertEqual(3, newBike.gear)


    def test_if_gear_follows_correct_range_for_speed_41_and_above(self):
        """
        Gear 1: 0 - 20
        b)Gear 2: 21 - 30 c) Gear 3: 31 - 40 d) Gear 4: 41 and above
        These gear changes automatically as soon as the bike gets exceeds any of these speed
        ranges either through acceleration or deceleration.
        """
        speed = list(range(41, 200))
        newBike.selectGearAutomatically(random.choice(speed))
        self.assertEqual(4, newBike.gear)


if __name__ == "__main__":
    unittest.main()

