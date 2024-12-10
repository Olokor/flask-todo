public class test{
    // public static void main(String[] args){
    //     for (int i=5; i>0; i--){
    //         System.out.println(i);
    //     }
    public static void main(String[] args) 
    { 
        // Integer i = new Integer(5); 
  
        // // Below line causes compile time error:- 
        // // Incompatible conditional operand types 
        // // Integer and String 
        // System.out.println(i instanceof String); 

        System.out.println(Integer.MAX_VALUE);
        int number = Integer.parseInt(System.console().readLine("enter number: "));

        long factorial = 1;
		if (number == 0){
			System.out.println(1);
		}
		for (int i=number; i>=1; i--){
			System.out.println("i is now "+i);
			factorial *=i;
		}
		System.out.println(factorial);
    }

}