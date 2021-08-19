package edu.bu.met.cs665;

/**
 * this class will work as part of the thread pool for running the supermarket.
 *
 * @author Zhaowei Gu
 * @version 1.0
 * @since 2021-08-18
 */
public class Cashier implements Runnable {

  private final CheckoutCounter checkout;

  public Cashier(final CheckoutCounter checkout) {
    this.checkout = checkout;
  }

  @Override
  public void run() {
    checkout.runMarket();
  }
}