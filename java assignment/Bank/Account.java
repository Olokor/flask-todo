import java.util.ArrayList;

public class Account {
    protected String accountName;
    private String address;
    private String BVN;
    private String phoneNumber;
    protected double accountBalance;
    protected String accountNumber;

    public Account(String accountName, double depositAmount, String address, String bvn, String phoneNumber) {
        this.accountName = accountName;
        this.accountBalance = depositAmount;
        this.address = address;
        this.BVN = bvn;
        this.phoneNumber = phoneNumber;
        this.accountNumber = (phoneNumber != null && phoneNumber.length() > 1) ? phoneNumber.substring(1) : "Invalid";
    }

    // a constructor that creates a zero account...
    public Account(String accountName, String address, String bvn, String phoneNumber) {
        this(accountName, 0.00, address, bvn, phoneNumber);
    }

    private  void accountDetails() {
        System.out.println("""
        Welcome to Dev_0 Banking Group PC...
        Below are your banking details for your account:
        """);
        System.out.println(String.format("Name: %s%nAccount Number: %s%nAccount Balance: %.2f%n",
                accountName, accountNumber, accountBalance));
    }

    private boolean depositMoney(double amount) {
        if (amount > 0) {
            this.accountBalance += amount;
            return true;
        }
        System.out.println("Invalid deposit amount.");
        return false;
    }

    private  boolean withdrawMoney(double amount) {
        if (amount > 0 && accountBalance >= amount) {
            accountBalance -= amount;
            return true;
        }
        System.out.println("Insufficient funds or invalid amount.");
        return false;
    }

    private boolean transferMoney(double amount, String accountNumber, ArrayList<Account> allAccounts) {
        if (amount <= 0 || this.accountBalance < amount) {
            System.out.println("Transfer failed: Invalid amount or insufficient balance.");
            return false;
        }

        for (Account user : allAccounts) {
            if (user.accountNumber.equals(accountNumber)) {
                this.accountBalance -= amount;
                user.accountBalance += amount;
                System.out.println("Transfer successful.");
                return true;
            }
        }
        System.out.println("Transfer failed: Account not found.");
        return false;
    }

    public void ussdOperation(ArrayList<Account> allAccounts){
        System.out.print("""
            welcome to Ussd service....
            1. check account balance
            2. recharge your line(data/arirtime)
            3. mobile transfer
            4. account details
            5. pay bills
            please pick a number for the menu >>>>>>>>> """);
            int input = Integer.parseInt(System.console().readLine());

            switch(input){
                case 1 -> {
                    System.out.println("your accountbalance is N"+this.accountBalance);
                }

                case 2 -> {
                    if(accountBalance > 0){
                        System.out.println("we are still developing this feature, but we have recharged your line with "+ accountBalance/15);

                    }else{
                        System.out.println("insufficient funds!");
                    }
                    
                    
                }
                case 3 -> {
                    String recipientAccountNumber = System.console().readLine("Enter account number");
                    double amount = Double.parseDouble(System.console().readLine("enter the amount you want to transfer>>>> "));
                    transferMoney(amount, recipientAccountNumber, allAccounts);
                }

                case 5 -> {
                    System.out.println("this service will be available soon");
                }
                default -> {
                    accountDetails();
                }
            }
    }
}
