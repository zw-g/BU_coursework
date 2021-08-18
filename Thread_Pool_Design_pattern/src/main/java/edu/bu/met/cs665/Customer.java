package edu.bu.met.cs665;

/**
 * this class will work as part of the thread pool for generating shopping list.
 *
 * @author Zhaowei Gu
 * @version 1.0
 * @since 2021-08-18
 */
public class Customer implements Runnable {

  private final CreateShoppingList create;

  public Customer(final CreateShoppingList create) {
    this.create = create;
  }

  @Override
  public void run() {
    create.write();
  }
}
