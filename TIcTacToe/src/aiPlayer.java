import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Random;

public class aiPlayer {

  int turnChecker;

  public int play(int[] input, int turnChecker) {
    //We can place the first ‘X’ randomly – as per a few online research papers on best opening
    // moves in Tic Tac Toe, an ‘X’ in any of the 0,2,6,8 corner spots is the best first move.
    if (input[0] == 0 && input[1] == 0 && input[2] == 0 && input[3] == 0 && input[4] == 0
        && input[5] == 0 && input[6] == 0 && input[7] == 0 && input[8] == 0) {
      int temp = new Random().nextInt(3 - 0 + 1) + 0;
      if (temp == 0) {
        return 0;
      } else if (temp == 1) {
        return 2;
      } else if (temp == 2) {
        return 6;
      } else {
        return 8;
      }
    }

    //[0] stores board location
    //[1] stores score
    this.turnChecker = turnChecker;
    List<int[]> bestPosition = new ArrayList<>();
    //add result into the list
    for (int i = 0; i < 9; i++) {
      int[] board = new int[]{input[0], input[1], input[2], input[3], input[4], input[5], input[6],
          input[7], input[8]};
      if (board[i] == 0) {
        board[i] = turnChecker;
        int winResult = Game.checkerWin(board);
        if (winResult == 0) {
          if (turnChecker == 1) {
            bestPosition.add(new int[]{i, miniMax(board, -1)});
          } else {
            bestPosition.add(new int[]{i, miniMax(board, 1)});
          }
        } else if (winResult == 2) {
          bestPosition.add(new int[]{i, miniMax(board, 0)});
        } else if (winResult == -1) {
          if (-1 == turnChecker) {
            bestPosition.add(new int[]{i, miniMax(board, 1)});
          } else {
            bestPosition.add(new int[]{i, miniMax(board, -1)});
          }
        } else {
          if (1 == turnChecker) {
            bestPosition.add(new int[]{i, miniMax(board, 1)});
          } else {
            bestPosition.add(new int[]{i, miniMax(board, -1)});
          }
        }
      }
    }

    //debug
    //return the mini for max result
    Collections.sort(bestPosition, new Comparator<int[]>() {
      @Override
      public int compare(int[] o1, int[] o2) {
        if (o1[1] == o2[1]) {
          return 0;
        } else if (o1[1] > o2[1]) {
          return -1;
        } else {
          return 1;
        }
      }
    });
    int x = bestPosition.get(0)[0];
    for (int n = bestPosition.size() - 1; n > 0; n--) {
      if (bestPosition.get(0)[1] > bestPosition.get(n)[1]) {
        bestPosition.remove(n);
      }
    }
    int index = (int) (Math.random() * bestPosition.size());
    return bestPosition.get(index)[0];
  }

  private int miniMax(int[] input, int turn) {
    List<Integer> score = new ArrayList<>();

    //add result into the list
    for (int i = 0; i < 9; i++) {
      int[] board = new int[]{input[0], input[1], input[2], input[3], input[4], input[5], input[6],
          input[7], input[8]};
      if (board[i] == 0) {
        board[i] = turn;
        int winResult = Game.checkerWin(board);
        if (winResult == 0) {
          if (turn == 1) {
            score.add(miniMax(board, -1));
          } else {
            score.add(miniMax(board, 1));
          }
        } else if (winResult == 2) {
          score.add(0);
        } else if (winResult == -1) {
          if (-1 == turnChecker) {
            score.add(1);
          } else {
            score.add(-1);
          }
        } else {
          if (1 == turnChecker) {
            score.add(1);
          } else {
            score.add(-1);
          }
        }
      }
    }

    if (score.size() > 0) {
      if (turn == turnChecker) {
        return Collections.max(score);
      } else {
        return Collections.min(score);
      }
    }
    return 0;
  }
}