import java.io.*;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class ProcessScheduling {
    /*Read data from the fileName in the file
    ArrayList, the list in which the process information is read
    The fileName, the file name
    The return value is null
    */
    public static void readFromFile(ArrayList<Process> arrayList, String fileName){
        String inputFile;
//        System.out.print("Please enter input file: ");
        inputFile = fileName;
//        inputFile = in.next();
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(new File(inputFile)));
            String line;
            //Read one line at a time
            while ((line = bufferedReader.readLine()) != null){
                if (line.length() == 0){
                    continue;
                }
                //Space off
                String []p = line.split(" ");
                //Four Numbers
                Integer []q = new Integer[4];
                //Convert a string to a number
                for (int i = 0; i < 4; i++){
                    q[i] = Integer.parseInt(p[i]);
                }
                //Create a new process
                arrayList.add(new Process(q[0],q[1],q[2],q[3]));
            }
            //Output process information
            for (int i = 0; i < arrayList.size(); i++){
                System.out.println(arrayList.get(i));
            }
        }catch (IOException e){

        }
    }
    public static void main(String []args) throws FileNotFoundException {
        int currentTime;
        boolean running;
        ArrayList<Process> arrayList;
        int MaxWaitTime;
        double sum;
        int n;

        PrintStream ps = new PrintStream("./process_scheduling_output.txt");
        System.setOut(ps);
        //Initializes the total time
        sum = 0;
        //Initializes the maximum wait time
        MaxWaitTime = 30;
        //Initialize process ArrayList
        arrayList = new ArrayList<>();
        //Read data from a file
        readFromFile(arrayList, args[0]);
        System.out.println("");
        System.out.println("Maximum wait time = 30");
        System.out.println("");
        //Find the minimum start time
        currentTime = Integer.MAX_VALUE;
        n = arrayList.size();
        running = false;
        PriorityQueue<Process> priorityQueue = new PriorityQueue<>();
        for (int i = 0; i < arrayList.size(); i++){
            currentTime = Math.min(currentTime, arrayList.get(i).arrivalTime);
        }
        Process process = null;
        //Continue when the priority queue is not empty or the process list is not empty
        while (arrayList.size() != 0 || priorityQueue.size() != 0){
            //When the process list is not empty, all processes whose arrival time is less than the current time are removed from the process list and added to the priority queue
            while (arrayList.size() != 0){
                int id = 0;
                for (int i = 1; i < arrayList.size(); i++){
                    if (arrayList.get(i).arrivalTime < arrayList.get(id).arrivalTime){
                        id = i;
                    }
                }
                Process p = arrayList.get(id);
                if (p.arrivalTime <= currentTime){
                    priorityQueue.add(p);
                    arrayList.remove(id);
                }else{
                    break;
                }
            }
            //If the priority queue is not empty
            if (!priorityQueue.isEmpty()){
                //Delete priority queue first
                Process p = priorityQueue.poll();
                //Output the corresponding information
                System.out.printf("Process removed from queue is: id = %d, at time %d, " +
                                "wait time = %d Total wait time = %.1f\n", p.id, currentTime,
                        currentTime - p.arrivalTime, sum);
                System.out.printf("Process id = %d\n", p.id);
                System.out.printf("Priority = %d\n", p.pr);
                System.out.printf("Arrival = %d\n", p.arrivalTime);
                System.out.printf("Duration = %d\n", p.duration);
                sum += currentTime - p.arrivalTime;
                currentTime += p.duration;
                System.out.printf("Process %d finished at time %d\n", p.id, currentTime);
                System.out.println("");
                System.out.println("Update priority:");
//                for (int i = 0; i < arrayList.size(); i++){
//                    if (currentTime - arrayList.get(i).arrivalTime > MaxWaitTime){
//                        System.out.printf("PID = %d, wait time = %d, current priority = %d\n",
//                                arrayList.get(i).id, currentTime - arrayList.get(i).arrivalTime,
//                                arrayList.get(i).pr);
//                        arrayList.get(i).pr--;
//                        System.out.printf("PID = %d, new priority = %d\n", arrayList.get(i).id, arrayList.get(i).pr);
//                    }
//                }
                ArrayList<Process> processes = new ArrayList<>();
                while (!priorityQueue.isEmpty()){
                    processes.add(priorityQueue.poll());
                }
                //For wait times longer than 30 minutes, update the priority
                for (int i = 0; i < processes.size(); i++){
                    if (currentTime - processes.get(i).arrivalTime > MaxWaitTime){
                        System.out.printf("PID = %d, wait time = %d, current priority = %d\n",
                                processes.get(i).id, currentTime - processes.get(i).arrivalTime,
                                processes.get(i).pr);
                        processes.get(i).pr--;
                        System.out.printf("PID = %d, new priority = %d\n", processes.get(i).id, processes.get(i).pr);
                    }
                    priorityQueue.add(processes.get(i));
                }
                System.out.println("");
            }else if (arrayList.size() != 0){       //The priority queue is empty and currentTime is updated to the minimum process arrival time in the ArrayList
                int id = 0;
                for (int i = 1; i < arrayList.size(); i++){
                    if (arrayList.get(i).arrivalTime < arrayList.get(id).arrivalTime){
                        id = i;
                    }
                }
                Process p = arrayList.get(id);
                currentTime = p.arrivalTime;
            }
        }
        System.out.printf("Total wait time = %.1f\n", sum);
        System.out.printf("Average wait time = %.1f\n", sum / n);
    }
}
//Process of class
class Process implements Comparable<Process>{
    public Integer pr;
    public Integer id;
    public Integer arrivalTime;
    public Integer duration;
    public Process(Integer id, Integer pr, Integer duration, Integer arrivalTime){
        this.id = id;
        this.pr = pr;
        this.arrivalTime = arrivalTime;
        this.duration = duration;
    }
    //Override the toString method
    //Output process information
    @Override
    public String toString() {
        return "Id = " + id + ", priority = " + pr + ", duration = " + duration + ", arrival time = " + arrivalTime + "";
    }
    //Overloaded comparison method
    @Override
    public int compareTo(Process o) {
        return pr.compareTo(o.pr);
    }
}