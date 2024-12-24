
import java.util.ArrayList;


public class AccountManager{
    private ArrayList<CreateAccount> accounts = new ArrayList<>();

    private void createAccount(){
        System.out.println("""
        hello, welocome to our mobile banking service
        we are dedicated to providing you with the best experience and managing your money..
        please fill this form to create your account""");

        String accountName = System.console().readLine("enter your full name>>>> ");
        String address = System.console().readLine("Enter your residental address>>> ");
        String phoneNumber = System.console().readLine("ENter your phone number>>>> ");
        String bvn = System.console().readLine("Enter your BVN>>> ");
        String pin = System.console().readLine("Enter pin>>> ");

        while (true) { 
            if (checkPin(pin)){
                break;
            }
            System.out.println("invalid pin combination! /n pin must contain 4 numbers only");
            pin = System.console().readLine("Enter pin>>> ");
        }

        // check if user wants a zero account or want to deposit money when opening the account
        String response = System.console().readLine("do you want to deposit money in your account y/n?: ").toLowerCase();
        if (response.equals("yes") || response.equals("y")){
            double amount = Double.parseDouble((System.console().readLine("enter amount>>> ")));
            CreateAccount newAccount = new CreateAccount(accountName, address, phoneNumber, amount, bvn, pin);
            accounts.add(newAccount);

        }else{
            // create zero account
            CreateAccount newAccount = new CreateAccount(accountName, address, phoneNumber, bvn, pin);
            accounts.add(newAccount);

        }
    }

    private CreateAccount login(){
       System.out.println("your Login details are your account number and pin....");
       String userId = System.console().readLine("enter your account number>>> ");
       String pin = System.console().readLine("enter your pin>>> ");
        for (CreateAccount account: this.accounts){
            if ((account.accountNumber == null ? userId == null : account.accountNumber.equals(userId)) || (account.pin == null ? pin == null : account.pin.equals(pin))){
                return account;
            }
        }
        return null;
        
    }
    private CreateAccount getUserDetails(String accountNumber){
        for (CreateAccount account: this.accounts){
            if (account.accountNumber.equals(accountNumber)){
                return account;
            }
        }
        return null;
    }

    private void transferMoney(double amount, String accountNumber){
        CreateAccount account = getUserDetails(accountNumber);
        if (account == null){
            System.out.println("account nor found!");
        }else{
            account.accountBalance += amount;
        }

    }

    private void withdrawMoney(double amount, CreateAccount account){
        account.accountBalance -= amount;
    }

    private double getBalance(CreateAccount account){
        return account.accountBalance;
    }

    private void rechargeLine(double amount, CreateAccount account){
        System.out.println("your recharge is on it way...");
        account.accountBalance -= amount;
    }

    private void rechargeLine(double amount, String phoneNumber, CreateAccount account){
        System.out.println("your recharge is on it way to " +phoneNumber);
        account.accountBalance -= amount;
    }

    private static boolean checkPin(String pin){
        if (pin.length() == 4){
            try {
                int pinInt = Integer.parseInt(pin);
                return true;
            } catch (NumberFormatException e) {
                return false;
            }
        }
        return false;
    }

    public void ussd() {
    System.out.println("""
        Welcome to the USSD interface.
        1. Create account
        2. Check account balance
        3. Withdraw money
        4. Recharge line (personal)
        5. Recharge line (external)
        6. Login
        >>>>>> """);

    String input = System.console().readLine();
    CreateAccount loggedInUser = null;

    switch (input) {
        case "1" -> {
            String response;
            do {
                createAccount();
                response = System.console().readLine("Do you want to create another account? y/n? ").toLowerCase();
            } while ("y".equals(response) || "yes".equals(response));

            // Prompt the user to log in after creating accounts
            loggedInUser = login();
            System.out.println(accounts);
        }

        case "6" -> loggedInUser = login();

        default -> System.out.println("Invalid option. Please try again.");
    }

    if (loggedInUser == null) {
        System.out.println("Please log in to continue.");
        return;
    }

    // Allow user to perform operations
    while (true) {
        System.out.println("""
            Welcome to the USSD interface.
            1. Check account balance
            2. Withdraw money
            3. transfer money
            4. Recharge line (personal)
            5. Recharge line (external)
            6. Exit
            >>>>>> """);

        String prompt = System.console().readLine();

        switch (prompt) {
            case "1" -> {
                double balance = getBalance(loggedInUser);
                System.out.println("Your current balance is: " + balance);
            }

            case "2" -> {
                try {
                    double amount = Double.parseDouble(System.console().readLine("Enter amount>>> "));
                    if (loggedInUser.accountBalance >= amount) {
                        withdrawMoney(amount, loggedInUser);
                        System.out.println("Transaction successful.");
                        System.out.println("Your current balance is: " + loggedInUser.accountBalance);
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid amount entered.");
                }
            }

            case "3" -> {
                try {
                    double amount = Double.parseDouble(System.console().readLine("Enter amount>>> "));
                    String accountNumber = System.console().readLine("Enter account number>>> ");
                    if (loggedInUser.accountBalance >= amount) {
                        transferMoney(amount, accountNumber);
                        System.out.println("Transaction successful.");
                        System.out.println("Your current balance is: " + loggedInUser.accountBalance);
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid amount entered.");
                }
            }

            case "4" -> {
                try {
                    double amount = Double.parseDouble(System.console().readLine("Enter amount>>> "));
                    if (loggedInUser.accountBalance >= amount) {
                        rechargeLine(amount, loggedInUser);
                        System.out.println("Transaction successful.");
                        System.out.println("Your current balance is: " + loggedInUser.accountBalance);
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid amount entered.");
                }
            }

            case "5" -> {
                try {
                    double amount = Double.parseDouble(System.console().readLine("Enter amount>>> "));
                    String phoneNumber = System.console().readLine("Enter recipient phone number>>> ");
                    if (loggedInUser.accountBalance >= amount) {
                        rechargeLine(amount, phoneNumber, loggedInUser);
                        System.out.println("Transaction successful.");
                        System.out.println("Your current balance is: " + loggedInUser.accountBalance);
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid amount entered.");
                }
            }

            case "6" -> {
                System.out.println("Thank you for using our USSD service. Goodbye!");
                return;
            }

            default -> System.out.println("Invalid option. Please try again.");
        }
    }
}

}


    


