import java.util.*;

public class Hw4_P6 {
    public static void main(String[] args) {
        //create a HashMap instance myMap
        HashMap<Integer, Integer> myMap = new HashMap<Integer, Integer>();
        //create an ArrayList instance myArrayList
        ArrayList<Integer> myArrayList = new ArrayList<Integer>();
        //create a LinkedList instance myLinkedList
        LinkedList<Integer> myLinkedList = new LinkedList<Integer>();

        long myMapTime = 0;
        long myArrayListTime = 0;
        long myLinkedListTime = 0;
        long myMapTime2 = 0;
        long myArrayListTime2 = 0;
        long myLinkedListTime2 = 0;

        System.out.println("The program is running it might take a while please wait.");
        //Repeat the following 10 times and calculate average total insertion time and average total search time for each data structure
        for (int i = 0; i < 10; i++) {
            //generate 100,000 distinct random integers in the range [1, 1,000,000] and store them in the array of integers insertKeys[ ]
            int[] insertKeys = new int[100000];
            for (int x = 0; x < insertKeys.length; x++) {
                insertKeys[x] = (int) (Math.random() * 1000000 + 1);
            }//end for loop

            // begin with empty myHap, myArrayList, and myLinkedList each time
            myMap.clear();
            myArrayList.clear();
            myLinkedList.clear();

            // Insert keys one at a time but measure only the total time (not individual insert time)
            // Use put method for HashMap, e.g., myMap.put(insertKeys[i], i)
            // Use add method for ArrayList and LinkedList

            //insert all keys in insertKeys [ ] into myMap and measure the total insert time
            long startTime = System.nanoTime();
            for (int x : insertKeys) {
                myMap.put(x, x);
            }
            long endTime = System.nanoTime();
            long timeElapsed = endTime - startTime;
            myMapTime = myMapTime + timeElapsed;

            //insert all keys in insertKeys [ ] into  myArrayList and measure the total insert time
            startTime = System.nanoTime();
            for (int x : insertKeys) {
                myArrayList.add(x);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
            myArrayListTime = myArrayListTime + timeElapsed;

            //insert all keys in insertKeys [ ] into myLinkedList and measure the total insert time
            startTime = System.nanoTime();
            for (int x : insertKeys) {
                myLinkedList.add(x);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
            myLinkedListTime = myLinkedListTime + timeElapsed;

            //generate 100,000 distinct random integers in the range [1, 2,000,000] and store them in the array searchKeys[ ]
            int[] searchKeys = new int[100000];
            for (int x = 0; x < searchKeys.length; x++) {
                searchKeys[x] = (int) (Math.random() * 2000000 + 1);
            }//end for loop

            // Search keys one at a time but measure only total time (not individual search // time)
            // Use containsKey method for HashMap
            // Use contains method for ArrayList and Linked List

            //search myMap for all keys in searchKeys[ ] and measure the total search time
            startTime = System.nanoTime();
            for (int x : searchKeys) {
                myMap.containsKey(x);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
            myMapTime2 = myMapTime2 + timeElapsed;

            //search myArrayList for all keys in searchKeys[ ] and measure the total search time

            startTime = System.nanoTime();
            for (int x : searchKeys) {
                myArrayList.contains(x);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
            myArrayListTime2 = myArrayListTime2 + timeElapsed;

            //search myLinkedList for all keys in searchKeys[ ] and measure the total search time
            startTime = System.nanoTime();
            for (int x : searchKeys) {
                myLinkedList.contains(x);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
            myLinkedListTime2 = myLinkedListTime2 + timeElapsed;

            //System.out.println(myMap.size());
            //System.out.println(myArrayList.size());
            //System.out.println(myLinkedList.size());
        }

        System.out.println("Number of keys = 100000\n");
        System.out.println("HashMap average total insert time = " + myMapTime/10 + "ns");
        System.out.println("ArrayList average total insert time = " + myArrayListTime/10 + "ns");
        System.out.println("LinkedList average total insert time = " + myLinkedListTime/10 + "ns\n");
        System.out.println("HashMap average total search time = " + myMapTime2/10 + "ns");
        System.out.println("ArrayList average total search time = " + myArrayListTime2/10 + "ns");
        System.out.println("LinkedList average total search time = " + myLinkedListTime2/10 + "ns");
    }
}
