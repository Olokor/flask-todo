public class CreateAccount{
    String accountName;
    String address;
    String phoneNumber;
    String BVN;
    double accountBalance;
    String accountNumber;
    String pin;
    
    // constructor for nonZero account
    public CreateAccount(String accountName, String address, String phoneNumber, double depositAmount, String bvn, String pin){
        this.accountName = accountName;
        this.address = address;
        this.phoneNumber = (phoneNumber !=null && phoneNumber.length() >= 11)? phoneNumber.substring(1):"invalid phone number";
        this.BVN = bvn;
        depositAmount = this.accountBalance;
        this.accountNumber = this.phoneNumber;
        this.pin = pin;
    }

    // constructor for a zero account
    public CreateAccount(String accountName, String address, String phoneNumber, String bvn, String pin){
        this(accountName, address, phoneNumber, 0.00, bvn, pin);
        this.accountNumber = this.phoneNumber;
        this.pin = pin;
    }

    @Override
    public String toString() {
        return "{" +
                "accountName='" + accountName + '\'' +
                ", address='" + address + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", balance=" + this.accountBalance +
                ", bvn='" + BVN + '\'' +
                '}';
    }

}