import java.util.*;

public class Hw5_P7 {

     /* i got the code from the following website
     * textbook Data Structures and Algorithms in Java 6th Edition*/
    public static void insertionSort(int[] data){
        int n = data.length;
        for (int k = 1; k < n; k++) {     // begin with second character
            int cur = data[k];           //time to insert cur=data[k]
            int j = k;                    // find correct index j for cur
            while(j>0 && data[j-1]>cur){  // thus, data[j-1] must go after cur
                data[j] = data[j-1];      // slide data[j-1] rightward
                j--;                      // and consider previous j for cur
            }
            data[j] = cur;                // this is the proper place for cur
        }
    }

    /* i got the code from the following website
     * https://www.educative.io/edpresso/how-to-implement-a-merge-sort-in-java */
    public static void merge(int[] left_arr,int[] right_arr, int[] arr,int left_size, int right_size){
        int i=0,l=0,r = 0;
        //The while loops check the conditions for merging
        while(l<left_size && r<right_size){
            if(left_arr[l]<right_arr[r]){
                arr[i++] = left_arr[l++];
            }
            else{
                arr[i++] = right_arr[r++];
            }
        }
        while(l<left_size){
            arr[i++] = left_arr[l++];
        }
        while(r<right_size){
            arr[i++] = right_arr[r++];
        }
    }

    /* i got the code from the following website
     * https://www.educative.io/edpresso/how-to-implement-a-merge-sort-in-java */
    public static void mergeSort(int [] arr, int len){
        if (len < 2){return;}
        int mid = len / 2;
        int [] left_arr = new int[mid];
        int [] right_arr = new int[len-mid];
        //Dividing array into two and copying into two separate arrays
        int k = 0;
        for(int i = 0;i<len;++i){
            if(i<mid){
                left_arr[i] = arr[i];
            }
            else{
                right_arr[k] = arr[i];
                k = k+1;
            }
        }
        // Recursively calling the function to divide the subarrays further
        mergeSort(left_arr,mid);
        mergeSort(right_arr,len-mid);
        // Calling the merge method on each subdivision
        merge(left_arr,right_arr,arr,mid,len-mid);
    }

    /* i got the code from the following website
     * https://www.educative.io/edpresso/how-to-implement-quicksort-in-java */
    public static int[] QuickSort(int[] arr, int elements) {
        if(elements < 2){     //Base Case
            return arr;
        }
        int current_position=0;   //position of pivot element
        int temp; //a temporary variable to assist in swapping
        for(int i=1; i<elements; i++) //Partitioning loop
        {
            if(arr[i] <= arr[0])
            {
                current_position++;
                temp = arr[i];
                arr[i] = arr[current_position];
                arr[current_position] = temp;
            }
        }
        temp = arr[0]; 
        arr[0] = arr[current_position]; 
        arr[current_position] = temp; //Brings pivot to it's appropriate position

        int[] left = QuickSort(arr,current_position); //sorts the elements to the left of pivot
        int[] arr2 = Arrays.copyOfRange(arr, current_position+1, elements);//separates elements right of pivot
        int[] right = QuickSort(arr2, elements-current_position-1); //sorts the elements to the right of pivot
        int[] final_array = new int[elements]; //final array, to merge everything together

        for(int i=0; i<current_position; i++)
        {
            final_array[i] = left[i]; 
        }
        final_array[current_position] = arr[current_position];
        for(int i=current_position+1; i<elements; i++)
        {
            final_array[i] = right[i-current_position-1];
        }

        return final_array;
    }

    /* i got the code from the following website
     * https://www.geeksforgeeks.org/heap-sort/ */
    public void sort(int arr[])
    {
        int n = arr.length;
 
        // Build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
 
        // One by one extract an element from heap
        for (int i = n - 1; i > 0; i--) {
            // Move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
 
            // call max heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }
 
    /* i got the code from the following website
     * https://www.geeksforgeeks.org/heap-sort/ */
    // To heapify a subtree rooted with node i which is
    // an index in arr[]. n is size of heap
    void heapify(int arr[], int n, int i)
    {
        int largest = i; // Initialize largest as root
        int l = 2 * i + 1; // left = 2*i + 1
        int r = 2 * i + 2; // right = 2*i + 2
 
        // If left child is larger than root
        if (l < n && arr[l] > arr[largest])
            largest = l;
 
        // If right child is larger than largest so far
        if (r < n && arr[r] > arr[largest])
            largest = r;
 
        // If largest is not root
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
 
            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        //System.out.println("The program is running it might take a while please wait.");
        Hw5_P7 heapSort = new Hw5_P7(); 
        String[][] output = new String[5][11];

        //add to the output
        output[0][0] = "Algorithm/n";
        output[1][0] = "insertion";
        output[2][0] = "merge";
        output[3][0] = "quick";
        output[4][0] = "heapsort";

        //loop 10 time each time adding 10000
        for (int n = 10000; n <= 100000; n = n + 10000) {
            int[] randomArray = new int[n];
            //Create an array of n random integers between 1 and 1,000,000
            for (int x = 0; x < randomArray.length; x++) {
                randomArray[x] = (int) (Math.random() * 1000000 + 1);
            }//end for loop

            //add to the output
            output[0][n/10000] = Integer.toString(n);

            //Run insertionsort and calculate the elapsed time
            int a[] = randomArray.clone();
            long startTime = System.currentTimeMillis();
            insertionSort(a);
            long endTime = System.currentTimeMillis();
            long timeElapsed = endTime - startTime;
            output[1][n/10000] = Long.toString(timeElapsed);    //add to the output

            //Run mergesort and calculate the elapsed time
            a = randomArray.clone();
            startTime = System.currentTimeMillis();
            mergeSort(a,a.length);
            endTime = System.currentTimeMillis();
            timeElapsed = endTime - startTime;
            output[2][n/10000] = Long.toString(timeElapsed);

            //Run quicksort and calculate the elapsed time
            a = randomArray.clone();
            startTime = System.currentTimeMillis();
            QuickSort(a,a.length);
            endTime = System.currentTimeMillis();
            timeElapsed = endTime - startTime;
            output[3][n/10000] = Long.toString(timeElapsed);    //add to the output

            //Run heapsort and calculate the elapsed time
            a = randomArray.clone();
            startTime = System.currentTimeMillis();
            //heap-sort
            heapSort.sort(a);
            endTime = System.currentTimeMillis();
            timeElapsed = endTime - startTime;
            output[4][n/10000] = Long.toString(timeElapsed);    //add to the output
        }

        //print the result
        for(int i = 0; i<5; i++){
            for(int j = 0; j < 11; j++){
                System.out.print(output[i][j]);
                if (j == 0) {
                    for(int m = 0; m<(12-output[i][j].length()); m++){
                        System.out.print(" ");
                    }
                }
                else if (j < 10) {
                    for(int m = 0; m<(6-output[i][j].length()); m++){
                        System.out.print(" ");
                    }
                }
                if(j != 10)System.out.print("| ");
            }
            System.out.println("\n--------------------------------------------------------------------------------------------");
        }
    }
}
