package edu.bu.met.cs665;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.Random;
import org.jetbrains.annotations.NotNull;

/**
 * this class will work as part of the thread pool for generating shopping list.
 *
 * @author Zhaowei Gu
 * @version 1.0
 * @since 2021-08-18
 */
public class CreateShoppingList {

  String[] arrOfItems;
  int minBuyAmount;
  int maxBuyAmount;
  String output = "";

  /**
   * <h3>Create a shopping list into the shoppingList.txt file</h3>
   *
   * @param arrOfItems   store items array, main input
   * @param minBuyAmount min line size
   * @param maxBuyAmount max line size
   */
  public CreateShoppingList(String @NotNull [] arrOfItems, int minBuyAmount, int maxBuyAmount) {
    this.arrOfItems = arrOfItems.clone();
    this.minBuyAmount = minBuyAmount;
    this.maxBuyAmount = maxBuyAmount;
  }

  /**
   * This method will randomly write for n length from items array into the shoppingList.txt.
   */
  public void write() {
    // write input file <<shoppingList>>
    Writer myWriter = null;
    try {
      myWriter = new OutputStreamWriter(new FileOutputStream("shoppingList.txt", true),
          StandardCharsets.UTF_8);
      for (int x = 0; x < new Random().nextInt(maxBuyAmount - minBuyAmount + 1)
          + minBuyAmount; x++) {
        output += arrOfItems[new Random().nextInt(100)] + ",";
      }
      output += "\n";
      myWriter.write(output);
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
}
