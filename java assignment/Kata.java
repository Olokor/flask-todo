public class kata{
	
	public static void main(String[] args){
		System.out.println(isEven(90));	
		System.out.println(isPrime(10));
		System.out.println(subtarctNumbers(7,3));
		System.out.println(divideNumbers(8.0f,2.0f));
		System.out.println(factorOf(80));
		System.out.println(isPerfectSquare(25));
		System.out.println(isPalindrome("aga"));
		System.out.println(factorialOf(5	));




	}

	public static boolean isEven(Integer number){
		return number % 2 == 0;
	}
	
	public static boolean isPrime(Integer number){
		for(int divisor=2; divisor<=number-2; divisor++){
			if (number % divisor == 0){
				return false;
			}
		}
		
		return true;
	
	}
	
	public static int subtarctNumbers(int firstNumber, int secondNumber){
		if (firstNumber > secondNumber){

			return (firstNumber - secondNumber);
		}
		return (secondNumber - firstNumber);
	
	}

	public static float divideNumbers(float firstNumber, float secondNumber){
		return (firstNumber/secondNumber);

	}

	public static int factorOf(int number){
		int count = 0;
		for(int divisor=1; divisor <= number; divisor++){
			if (number % divisor == 0){
				System.out.print(divisor);
				System.out.print(",");
				count++;
			}
		}
		System.out.println();	
		return count;
	}

	public static boolean isPerfectSquare(int number){
		for (int i=1; i<=number; i++){
			if (i*i == number){
				return true;
			}
		}
		return false;
	}

	public static boolean isPalindrome(String word){
		String reverse_word = "";
		for(int i=0; i<word.length(); i++){
			char character = word.charAt(i);
			reverse_word = character + reverse_word;
		}
		System.out.println(reverse_word);
		return word.equals(reverse_word);
	}

	public static long factorialOf(int number){
		long factorial = 1;
		if (number == 0){
			return 1;
		}
		for (int i=number; i>=1; i--){
			// System.out.println("i is now "+i);
			factorial *=i;
		}
		return factorial;
	}
}
	

	
