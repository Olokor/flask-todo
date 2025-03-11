public class QuadraticEquationSolver {
    public static void main(String[] args) {
        double root1, root2;
//        ax^2 -bx - 5 = 0
        double a = Double.parseDouble(System.console().readLine("Enter the value of a: "));
        double b = Double.parseDouble(System.console().readLine("Enter the value of b: "));
        double c = Double.parseDouble(System.console().readLine("Enter the value of c: "));

        double d = (b*b) - (4*a*c);

        if (d==0){
            System.out.println("The equation has one real solution");
            root1 = root2 = (-b+Math.sqrt(d))/(2*a);
            System.out.println("the root of the equation are "+root1+" "+ root2);
        }else if (d>0){
            System.out.println("The equation has two real solutions");
            root1 = (-b + Math.sqrt(d))/(2*a);
            root2 = (-b - Math.sqrt(d))/(2*a);
            System.out.println("the root of the equation are "+root1+" "+ root2);
        }else{
            System.out.println("The equation has one real solution");
            root1 = (-b + Math.sqrt(d))/(2*a);
            root2 = (-b - Math.sqrt(d))/(2*a);
            System.out.println("the root of the equation are "+root1+" "+ root2);
        }
    }

}
