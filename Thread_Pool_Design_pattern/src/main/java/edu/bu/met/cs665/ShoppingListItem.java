package edu.bu.met.cs665;

class ShoppingListItem {

  private final String item;
  private final float price;
  private int quantity;

  public ShoppingListItem(String item, float price) {
    this.item = item;
    this.price = price;
    this.quantity = 1;
  }

  //getter and add method
  public String getItem() {
    return item;
  }

  public float getPrice() {
    return price;
  }

  public int getQuantity() {
    return quantity;
  }

  public void addQuantity() {
    quantity += 1;
  }
}