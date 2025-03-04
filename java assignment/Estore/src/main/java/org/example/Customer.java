package org.example;

import java.util.ArrayList;
import java.util.List;

public class Customer extends User {

    private List<Product> shoppingCart = new ArrayList<>();
    private CreditCardInformation cardDetails;
    public Customer(int age, String name, String email, String homeAddress, String phoneNumber,
                    int cvv, String expMonth, String expYear, String cardNumber) {
        super(age, name, email, homeAddress, phoneNumber);
        this.cardDetails = new CreditCardInformation(cvv, expMonth, expYear, cardNumber);
    }



    public List<Product> getShoppingCart() {
        return shoppingCart;
    }

    public void addToShoppingCart(Items item) {
        shoppingCart.add(item);
    }


    public CreditCardInformation getCardDetails() {
        return cardDetails;
    }
}


