package org.example;

import java.util.ArrayList;
import java.util.List;

public class Estore {
    public static void main(String[] args) {
        List<Product> ElectronicProduct = new ArrayList<>(List.of(
                new Product(1, "OX fan", "Electric standing fan + rechargable",
                        ProductCategory.ELECTRONIC, 70000.00),

                new Product(2, "Samsung s31", "2027 smartest android phone with the best camera and battery life",
                        ProductCategory.ELECTRONIC, 9500000),

                new Product(3, "ZARA", "mature clothing brand", ProductCategory.CLOTHING, 45000),

                new Product(4, "Butcher knife", "chop that meat in seconds",
                        ProductCategory.UTILITIES, 987.00)
        ));

        Customer customer = new Customer(65, "olokor emmanuel", "emmanuel@mail.com", "addresss", "08121324286", 222, "08", "23", "4567899087");
        System.out.println(customer.getCardDetails());

    }
}
