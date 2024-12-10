// import java.lang.reflect.Array;
import java.util.Arrays;

public class ArrayKata{
    public static void main(String[] args){
        double[] array = {2,4,6,89,3,90,34};
        int[] array2 = {2,3,4,5,67,8,9,0,};
        System.out.println(getMaximumValue(array));
        System.out.println(Arrays.toString(reverseArray(array)));
        System.out.println(checkIfValueInArray(array, 6));
        System.out.println(Arrays.toString(getOddPositionValues(array)));
        System.out.println(Arrays.toString(getEvenPositionValues(array)));


    }

    public static double getMaximumValue(double[] array){
        double maxValue = array[0];
        for (int i=1; i<array.length; i++){
            if (array[i] > maxValue) {
                maxValue = array[i];
            }
        }
        return maxValue;
    }

    public static double[] reverseArray(double[] array){
        double[] result = new double[array.length];
        int index = (array.length-1);
        for(int i=0; i<array.length; i++){
            result[index - i] = array[i];
        }
        return result;
    }

    public static boolean checkIfValueInArray(double[] array, double value){
        for(double element:array){
            if (element == value){
                return true;
            }
        }
        return false;
    }

    public static double[] getOddPositionValues(double[] array){
        double[] output = new double[(Integer)(array.length/2 + array.length%2)];
        int index = 0;
        for(int i=0; i<array.length; i+=2){
                output[index] = array[i];
                index++;
          
            }
             return output;
        }
    
    public static double [] getEvenPositionValues(double[] array){
        double[] output = new double[(Integer)(array.length/3 + array.length%3)];
        int index = 0;
        for(int i=1; i<array.length; i+=2){
                output[index] = array[i];
                index++;
          
            }
             return output;
    }

}