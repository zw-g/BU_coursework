import java.util.Scanner;

/**
 * <h1>Tic Tac Toe AI</h1>
 * <p>
 * We have designed a simple example of AI for Tic Tac Toe game, the main algorithm we have used is
 * MiniMax
 * </p>
 * <p>
 * this program and game interface run form the Run.java main method.
 * </p>
 *
 * @author Zhaowei Gu, Zheqian Zhang, Jianning Lu
 * @version 1.0
 * @since 2020-10-06
 */
public class Run {

  public static void main(String[] args) {
    System.out.println("Hi welcome to use Tic Tac Toe Game");
    option();
  }

  public static void option() {
    System.out.println("What would you like to do:");
    System.out.println("0. Human vs. Human");
    System.out.println("1. Human vs. Machine");
    System.out.println("2. Machine vs. Machine");
    System.out.println("3. End");
    Scanner scanner = new Scanner(System.in);
    System.out.print("Please select an option: ");
    int userInput = scanner.nextInt();

    if (userInput == 0) {
      //human vs human
      Game humanVsHuman = new Game(0);
      humanVsHuman.start();
      option();
    } else if (userInput == 1) {
      //human vs machine
      Game humanVsMachine = new Game(1);
      humanVsMachine.start();
      option();
    } else if (userInput == 2) {
      //machine vs machine
      System.out.print("How manny round would you like the machine to play? ");
      int numberOfRound = scanner.nextInt();
      Game machineVsMachine = new Game(2, numberOfRound);
      machineVsMachine.start();
      option();
    } else if (userInput == 3) {
      //end
      System.out.println("Game end\nThank you for using Tic Tac Toe Game");
    } else {
      System.out.println("wrong input please re-select an option");
      option();
    }
  }
}