package org.example;

public class AirConditional {
    private int powerState;
    private int temperature;
    public AirConditional() {
        this.powerState = 0;
        this.temperature = 16;
    }

    public void turnOn(){
        powerState = 1;
    }
    public void setPowerState(int powerState) {
        this.powerState = powerState;
    }
    public int getPowerState() {
        return powerState;
    }

    public void turnOff(){
        powerState = 0;
    }
    public int getTemperature() {
        return this.temperature;
    }

    public void increaseTemperature(int temperatureValue) {
        checkTemperature(temperatureValue);
    }

    public void decreaseTemperature(int temperatureValue) {
        checkTemperature(temperatureValue);
    }

    public void checkTemperature(int temperatureValue) {
        if(temperatureIsGreaterThan30(temperatureValue)){
            this.temperature = 30;
        } else if (temperatureIsLessThan16(temperatureValue)) {
            this.temperature = 16;
        }else {
            this.temperature = temperatureValue;
        }
    }
    private Boolean temperatureIsGreaterThan30(int temperatureValue) {
//        if (temperatureValue > 30){
//            return true;
//        }
//        return false;
        return temperatureValue > 30;
    }

    private Boolean temperatureIsLessThan16(int temperatureValue) {return temperatureValue < 16;}
}
