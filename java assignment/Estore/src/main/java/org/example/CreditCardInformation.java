package org.example;

class CreditCardInformation{
    private int cvv;
    private String expMonth;
    private String expYear;
    private String cardNumber;
    private CardType cardType;

    public CreditCardInformation(int cvv, String expMonth, String expYear, String cardNumber) {
        this.cvv = cvv;
        this.expMonth = expMonth;
        this.expYear = expYear;
        this.cardNumber = cardNumber;
        this.cardType = getCardType(cardNumber);
    }

    private CardType getCardType(String cardNumber) {
        if(tryCastCardNumberToInt(cardNumber)){
            if (cardNumber.charAt(0) == '4'){
                return CardType.VISA_CARD;
            }else if (cardNumber.charAt(0) == '5'){return CardType.MASTERCARD;}
            else if (cardNumber.charAt(0) == '3' && cardNumber.charAt(1) == '7'){return CardType.VERVE;}
        }

        throw new IllegalArgumentException("Invalid card number");
    }

    private boolean tryCastCardNumberToInt(String cardNumber) {
        try{
            Integer.parseInt(cardNumber);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

}