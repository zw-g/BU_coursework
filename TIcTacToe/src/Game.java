import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Game {
  /*
  0. Human vs. Human
  1. Human vs. Machine
  2. Machine vs. Machine
  */

  int type;
  int round = 0;
  int turn = -1;
  aiPlayer aiPlayer;

  public Game(int type) {
    this.type = type;
    aiPlayer = new aiPlayer();
  }

  public Game(int type, int round) {
    this.type = type;
    this.round = round;
    aiPlayer = new aiPlayer();
  }

  public static void printBoard(int[] input) {
    String[] board = new String[9];

    // iterating over an array
    for (int i = 0; i < input.length; i++) {
      // accessing each element of array
      if (input[i] == 1) {
        board[i] = "O";
      } else if (input[i] == -1) {
        board[i] = "X";
      } else {
        board[i] = " ";
      }
    }

    System.out.println("\n ----------- ");
    System.out.println("| " + board[0] + " | "
        + board[1] + " | " + board[2]
        + " |");
    System.out.println("|-----------|");
    System.out.println("| " + board[3] + " | "
        + board[4] + " | " + board[5]
        + " |");
    System.out.println("|-----------|");
    System.out.println("| " + board[6] + " | "
        + board[7] + " | " + board[8]
        + " |");
    System.out.println(" ----------- ");
  }

  public static int checkerWin(int[] input) {
    List<Integer> x = new ArrayList<>();
    List<Integer> o = new ArrayList<>();

    for (int i = 0; i < input.length; i++) {
      if (input[i] == -1) {
        x.add(i);
      } else if (input[i] == 1) {
        o.add(i);
      }
    }
    if (x.size() >= 3) {
      if (x.contains(0) && x.contains(3) && x.contains(6) ||
          x.contains(1) && x.contains(4) && x.contains(7) ||
          x.contains(2) && x.contains(5) && x.contains(8) ||
          x.contains(0) && x.contains(1) && x.contains(2) ||
          x.contains(3) && x.contains(4) && x.contains(5) ||
          x.contains(6) && x.contains(7) && x.contains(8) ||
          x.contains(0) && x.contains(4) && x.contains(8) ||
          x.contains(2) && x.contains(4) && x.contains(6)) {
        return -1;
      }
    }
    if (o.size() >= 3) {
      if (o.contains(0) && o.contains(3) && o.contains(6) ||
          o.contains(1) && o.contains(4) && o.contains(7) ||
          o.contains(2) && o.contains(5) && o.contains(8) ||
          o.contains(0) && o.contains(1) && o.contains(2) ||
          o.contains(3) && o.contains(4) && o.contains(5) ||
          o.contains(6) && o.contains(7) && o.contains(8) ||
          o.contains(0) && o.contains(4) && o.contains(8) ||
          o.contains(2) && o.contains(4) && o.contains(6)) {
        return 1;
      }
    }
    if (x.size() + o.size() > 8) {
      return 2;
    }
    return 0;
  }

  public static int placeMark(int[] input, int turn) {
    Scanner scanner = new Scanner(System.in);
    if (turn == -1) {
      System.out.println("X turn");
    } else {
      System.out.println("O turn");
    }
    System.out.print("place your mark (0-8): ");
    int userIn = scanner.nextInt();
    if (userIn == 0 && input[0] == 0) {
      return 0;
    } else if (userIn == 1 && input[1] == 0) {
      return 1;
    } else if (userIn == 2 && input[2] == 0) {
      return 2;
    } else if (userIn == 3 && input[3] == 0) {
      return 3;
    } else if (userIn == 4 && input[4] == 0) {
      return 4;
    } else if (userIn == 5 && input[5] == 0) {
      return 5;
    } else if (userIn == 6 && input[6] == 0) {
      return 6;
    } else if (userIn == 7 && input[7] == 0) {
      return 7;
    } else if (userIn == 8 && input[8] == 0) {
      return 8;
    } else {
      System.out.println("Sorry, wrong input please try again");
      return placeMark(input, turn);
    }
  }

  public void start() {
    round -= 1;
    //init the board
    int[] board = new int[]{0, 0, 0, 0, 0, 0, 0, 0, 0};
    int winningResult;

    do {
      if (type == 0) {
        printBoard(board);
        board[placeMark(board, turn)] = turn;
        if (turn == -1) {
          turn = 1;
        } else {
          turn = -1;
        }
      } else if (type == 1) {
        printBoard(board);
        if (turn == -1) {
          board[placeMark(board, turn)] = turn;
          turn = 1;
        } else {
          board[aiPlayer.play(board, turn)] = turn;
          turn = -1;
        }
      } else if (type == 2) {
        if (turn == -1) {
          board[aiPlayer.play(board, turn)] = turn;
          turn = 1;
        } else {
          board[aiPlayer.play(board, turn)] = turn;
          turn = -1;
        }
      }
      winningResult = checkerWin(board);
    } while (winningResult == 0);
    printBoard(board);

    if (winningResult == 1) {
      System.out.println("O win!");
    } else if (winningResult == -1) {
      System.out.println("X win!");
    } else {
      System.out.println("tie");
    }
    if (round > 0) {
      start();
    }
    if (type != 2) {
      System.out.print("another round? \n0. yes\n1. no\n");
      Scanner scanner = new Scanner(System.in);
      int userIn = scanner.nextInt();
      if (userIn == 0) {
        start();
      }
    }
  }
}
