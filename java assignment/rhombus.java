public class rhombus{
    public static void main(String[] args) {
        int numberOfLetters = Integer.parseInt(System.console().readLine("enter number of letters: "));
        int space = numberOfLetters;
        for (int i=0; i<=(numberOfLetters-1); i++){
            for (int s = 0; s < space; s++) {
                System.out.print(" ");
            }
            for (int j=0; j<=i; j++){
                System.out.print((char)(65+j));
            }

            for (int j=(64+i); j>=65; j--){
                System.out.print((char)(j));
            }
            System.out.println();
            space--;
        }
        space = 1;
        
        for (int i=(numberOfLetters-2); i>=0; i--){
            for (int s = 0; s < space; s++) {
                System.out.print(" ");
            }
            for (int j=0; j<=i; j++){
                System.out.print((char)(65 + j));
            }

            for (int j=(64+i); j>65; j--){
                System.out.print((char)(j));
            }
            System.out.println();
            space++;
            
        }
    }

   
}