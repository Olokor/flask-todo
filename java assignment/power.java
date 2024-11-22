public class power{
    public static void main(String[] args) {
        int n = Integer.parseInt(System.console().readLine("enter a number: "));
        System.out.println("a    b    power(a, b)");
        int power = 1;
        for (int a=1; a<=n; a++){
            for (int i=1; i<=(a); i++){
                power *= a; 
            }
            System.out.println(a+"    "+(a+1)+"    "+power);
            power = a+1;
        }
    }
}
