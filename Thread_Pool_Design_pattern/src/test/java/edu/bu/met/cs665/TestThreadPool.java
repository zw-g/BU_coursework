package edu.bu.met.cs665;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.junit.Test;
import org.junit.runner.OrderWith;
import org.junit.runner.manipulation.Alphanumeric;

@OrderWith(Alphanumeric.class)
public class TestThreadPool {

  static final int customerNumber = 10000;
  static final int minBuyAmount = 1;
  static final int maxBuyAmount = 50;
  static final int discountAppliesPercentage = 10;
  static final int discountPercentage = 10;
  static String[] inputList = new String[customerNumber];

  @Test
  public void aTestSettingUpShoppingList() {
    //generate shopping list from this array
    String[] arrOfItems = new String[]{"Avocado-5.99", "Lemon-0.79", "Apple-5.99",
        "HoneydewMelon-4.99", "Strawberries-3.99", "Bananas-1.38", "Blueberries-4.99",
        "Grapes-5.98", "Blackberries-3.49", "Watermelon-3.99", "Broccoli-2.59", "BabySpinach-2.29",
        "Lettuce-1.99", "RomaineHearts-3.99", "Potatoes-3.99", "Onion-2.49", "Celery-3.99",
        "GreenBeans-2.99", "Garlic-1.2", "Cucumber-0.79", "Sausages-3.29", "ChickenBreast-6.29",
        "ChickenThigh-4.99", "Shrimp-15.99", "GroundTurkey-5.99", "GroundBeef-6.89",
        "AtlanticSalmon-9.99", "PorkChop-5.49", "Bacon-4.69", "Ham-4.99", "Yogurt-1.00",
        "Eggs-4.99", "WholeMilk-6.97", "StringCheese-4.99", "ParmesanCheese-4.59",
        "HeavyWhipCream-2.19", "Butter-3.29", "GreekYogurt-4.99", "YakultProbioticDrink-3.49",
        "CreamCheese-2.99", "OrangeJuice-4.29", "AppleJuice-3.79", "LemonJuice-3.09",
        "CoconutWater-1.88", "PeachJuice-3.59", "Peet'sCoffee-12.99", "SpringWater-1.25",
        "Starbucks-5.39", "ArizonaGreenTea-2.99", "ColdBrew-3.99", "CokeZero-5.78", "CocaCola-9.18",
        "Pepsi-8.99", "Sprite-9.18", "MountainDew-8.99", "RootBeer-4.99",
        "GrapefruitSparklingwater-6.19", "SportsDrink-2.50", "OatMilk-4.08", "MilkShake-4.19",
        "PaperTowels-7.59", "Disinfectingwipes-4.47", "AllPurposeCleaner-3.69",
        "PeroxideToiletCleaner-3.39", "WindowCleaner-4.29", "MagicCleaner-5.99",
        "SurfaceCleaner-4.29", "ToiletPaper-3.98", "LaundryDetergent-8.79", "AntBaits-4.94",
        "Bleach-5.48", "SandwichBag-3.00", "AluminumFoil-4.99", "PlasticWrap-2.69",
        "LiquidHandWash-1.00", "DishSoap-3.99", "DishwasherDetergent-12.7", "FacialTissue-6.39",
        "OilSpray-6.29", "SteelScrubber-2.29", "Battery-14.16", "LightBulb-7.94",
        "UtilityHooks-14.97", "BandAid-6.88", "Mosquitooff-5.69", "Vaseline-2.19",
        "Allergycare-17.66", "VitaminD-9.99", "VitaminC-8.89", "Melatonin-10.03",
        "ColoredPencil-5.99", "Tape-10.99", "Notespads-9.99", "Ruledpaper-13.95",
        "FileOrganizer-6.44", "TrashBags-11.35", "BabyWipes-12.32", "Scissor-4.22",
        "WrappingPaper-14.99", "Card-3.49"};

    //get count of available cores, fixed core system, but it changes depends on your system.
    int coreCount = Runtime.getRuntime().availableProcessors();
    ExecutorService service = Executors.newFixedThreadPool(coreCount);

    //Create new file and empty the file
    try {
      new FileWriter("shoppingList.txt", false).close();
    } catch (IOException e) {
      e.printStackTrace();
    }

    //start running the code
    final long startTime = System.nanoTime();

    //submit tasks for execution
    for (int i = 0; i < customerNumber; i++) {
      service.execute(new Customer(
          new CreateShoppingList(arrOfItems, minBuyAmount, maxBuyAmount)));
    }

    // All tasks were executed, now start to shut down
    service.shutdown();
    while (!service.isTerminated()) {
      Thread.yield();
    }

    //register the time
    final long totalTime = System.nanoTime() - startTime;
    long timeInSecond = TimeUnit.SECONDS.convert(totalTime, TimeUnit.NANOSECONDS);

    //print conclusion of the supermarket day
    System.out.println(coreCount + " customer generated " + customerNumber + " shopping list\n"
        + "they done all these in about " + timeInSecond + " second\n");
  }

  @Test
  public void bTestSetUpExecutorsWithAvailableProcessors() {
    int coreCount = Runtime.getRuntime().availableProcessors();
    ExecutorService service = Executors.newFixedThreadPool(coreCount);
  }

  @Test
  public void cTestReadShoppingList() {
    try {
      Scanner myReader = new Scanner(new File("shoppingList.txt"), StandardCharsets.UTF_8);
      int count = 0;
      while (myReader.hasNextLine()) {
        inputList[count] = myReader.nextLine();
        count++;
      }
      myReader.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  @Test
  public void dTestRunningProgram() {
    int coreCount = Runtime.getRuntime().availableProcessors();
    ExecutorService service = Executors.newFixedThreadPool(coreCount);

    //Create new file and empty the file
    try {
      new FileWriter("supermarketReceipt.txt", false).close();
    } catch (IOException e) {
      e.printStackTrace();
    }

    //start running the code
    final long startTime = System.nanoTime();

    //submit tasks for execution
    for (String line : inputList) {
      service.execute(
          new Cashier(new CheckoutCounter(line, discountAppliesPercentage, discountPercentage)));
    }

    // All tasks were executed, now start to shut down
    service.shutdown();
    while (!service.isTerminated()) {
      Thread.yield();
    }

    //register the time
    final long totalTime = System.nanoTime() - startTime;
    long timeInSecond = TimeUnit.SECONDS.convert(totalTime, TimeUnit.NANOSECONDS);

    //print conclusion of the supermarket day
    System.out.println("Supermarket day finished with " + coreCount + " Cashier working together");
    System.out.println(
        "They have helped " + customerNumber + " customer in about " + timeInSecond + " second");
  }
}
