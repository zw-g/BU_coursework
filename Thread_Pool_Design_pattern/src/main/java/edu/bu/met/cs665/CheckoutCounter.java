package edu.bu.met.cs665;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * this class will work as part of the thread pool for running the supermarket.
 *
 * @author Zhaowei Gu
 * @version 1.0
 * @since 2021-08-18
 */
public class CheckoutCounter {

  private static final AtomicInteger idGenerator = new AtomicInteger();
  private final String shoppingListString;
  private final int id;
  private final int discountAppliesPercentage;
  private final int discountPercentage;
  private final List<ShoppingListItem> shoppingList = new ArrayList<>();
  private String receipt = "";

  /**
   * <h3>This Class will print customer receipt into supermarketReceipt.txt.</h3>
   *
   * @param shoppingListString        shopping list a line of string
   * @param discountAppliesPercentage store discount apply possibility percentage
   * @param discountPercentage        store how much discount will give to customer that are being
   *                                  picked
   */
  public CheckoutCounter(String shoppingListString, int discountAppliesPercentage,
      int discountPercentage) {
    this.id = idGenerator.incrementAndGet();
    this.shoppingListString = shoppingListString;
    this.discountAppliesPercentage = discountAppliesPercentage;
    this.discountPercentage = discountPercentage;
    scanningItems();
  }

  /**
   * adding information to receipt. call method to access information and add to the receipt.
   */
  public void runMarket() {
    receipt = receipt + "Customer " + id + " receipt\n";
    receipt = receipt + String.format("%-19s %5s %10.5s%n", "Item", "Qty", "Price");
    receipt = receipt + String.format("%-19s %5s %10.5s%n", "----", "---", "-----");
    processingPayments(discountAppliesPercentage, discountPercentage);
    Writer myWriter = null;
    try {
      myWriter = new OutputStreamWriter(new FileOutputStream("supermarketReceipt.txt", true),
          StandardCharsets.UTF_8);
      myWriter.write(receipt);
    } catch (IOException e) {
      e.printStackTrace();
    } finally {
      if (myWriter != null) {
        try {
          myWriter.flush();
        } catch (IOException e) {
          e.printStackTrace();
        }
        try {
          myWriter.close();
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
    }
  }

  //scan the string to array list
  private void scanningItems() {
    String[] arrOfStr = shoppingListString.split(",");
    for (String a : arrOfStr) {
      String[] items = a.split("-");
      int check = 0;
      for (ShoppingListItem item : shoppingList) {
        if (item.getItem().equals(items[0])) {
          item.addQuantity();
          check = 1;
          break;
        }
      }
      if (check == 0) {
        shoppingList.add(new ShoppingListItem(items[0], Float.parseFloat(items[1])));
      }
    }
  }


  //calculate final price
  private void processingPayments(int discountAppliesPercentage, int discountPercentage) {
    float total = 0;
    for (ShoppingListItem item : shoppingList) {
      receipt += String.format("%-19.19s %5d %10.2f%n", item.getItem(), item.getQuantity(),
          item.getPrice());
      total += (item.getQuantity() * item.getPrice());
    }
    //maybe add discount
    receipt = receipt + "------------------------------------\n";
    Random rand = new Random();
    if (rand.nextInt(100) <= discountAppliesPercentage - 1) {
      receipt += String.format("%-19s %5s %10.2f%n", "Discount:", "",
          -1 * total * (discountPercentage / 100.0));
      receipt += String.format("%-19s %5s %10.2f%n", "Total:", "",
          total - (total * (discountPercentage / 100.0)));
    } else {
      receipt += String.format("%-19s %5s %10.2f%n", "Total:", "", total);
    }
    receipt += "\n";
  }
}
