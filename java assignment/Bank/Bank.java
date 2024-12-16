import java.util.ArrayList;
public class Bank{
    public static void main(String[] args) {
        Account firstUser = new Account("Olokor Wisdom", "15 odofin street olodi apapa lagos",
        "2002155567", "2348121324286");

        Account secoundAccount = new Account("Uzochukwu ibe", 5000, "16 kukoyi olodi apapa lagos", "6667388939346", "09130990139");
        ArrayList<Account> allAccounts = new ArrayList<>();
        allAccounts.add(firstUser);
        allAccounts.add(secoundAccount);
        System.out.print("welcome, please dial *737# to see how our ussd banking interface looks like...>>>>> ");
        String userInput = System.console().readLine();
        if (userInput.equals("*737#*")){
            secoundAccount.ussdOperation(allAccounts);
        }else{
            System.out.println("invalid ussd code...");
        }
    }
}