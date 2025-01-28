package org.example;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
//import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.*;

public class AirConditionalTest {

    AirConditional newAC = new AirConditional();
    @Test
    public void checkIfTurnOnExist(){
        newAC.turnOn();
    }
    @Test
    public void checkIfAirConditionIsOn() {
        newAC.turnOn();
        assertEquals(1, newAC.getPowerState());
    }
    @Test
    public void checkIfTurnOffExist() {
        newAC.turnOff();
    }
    @Test
    public void checkIfAirConditionIsOff() {
        newAC.turnOff();
        assertEquals(0, newAC.getPowerState());
//        System.out.println("this happened");
    }

    @Test
    public void checkIfIncreaseTemperatureExist() {
        newAC.increaseTemperature(10);
    }
    @Test
    public void checkIfIncreaseTemperatureIncreasesTheTemperature() {
        newAC.increaseTemperature(19);
        assertEquals(19, newAC.getTemperature());
    }

    @Test
    public void checkIfDecreaseTemperatureExist() {
        newAC.decreaseTemperature(10);
    }

    @Test
    public void checkIfDecreaseTemperatureDecreasesTheTemperature() {
        newAC.decreaseTemperature(12);
        assertEquals(16, newAC.getTemperature());
    }

    @Test
    public void checkIfTemperatureExceeds30(){
        newAC.increaseTemperature(45);
        assertEquals(30, newAC.getTemperature());
    }
    
    @Test
    public void checkIfTemperaturePreceed16(){
        newAC.increaseTemperature(12);
        assertEquals(16, newAC.getTemperature());
    }


}