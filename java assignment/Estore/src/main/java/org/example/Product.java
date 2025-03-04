package org.example;

public class Product {
    private int productId;
    private String productName;
    private String productDescription;
    private double productPrice;
    private ProductCategory productCategory;

    public Product(int productId, String productName, String productDescription, ProductCategory productCategory, double productPrice) {
        this.productId = productId;
        this.productName = productName;
        this.productDescription = productDescription;
        this.productPrice = productPrice;
        setProductCategory(productCategory);
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public double getProductPrice() {
        return productPrice;
    }

    public void setProductPrice(double productPrice) {
        this.productPrice = productPrice;
    }

    public ProductCategory getProductCategory() {
        return productCategory;
    }

    public void setProductCategory(ProductCategory productCategory) {
        switch (productCategory){
            case CLOTHING -> this.productCategory = ProductCategory.CLOTHING;
            case ELECTRONIC -> this.productCategory = ProductCategory.ELECTRONIC;
            case UTILITIES -> this.productCategory = ProductCategory.UTILITIES;
            case GROCERIES -> this.productCategory = ProductCategory.GROCERIES;
        }
    }

    public String getProductDescription() {
        return productDescription;
    }

    public void setProductDescription(String productDescription) {
        this.productDescription = productDescription;
    }
}
