## Processce Scheduling - Java

## How to run

javac ProcessScheduling.java

Java ProcessScheduling path to process_scheduling_input.txt{
	//such as
	java ProcessScheduling /Users/zhaoweigu/Downloads/src/process_scheduling_input.txt
}

## Data structure used

1. First of all, I built a class called Process to store Process information. This class
overloaded the toString method to output Process information and overloaded the
compareTo method to compare the size of two processes to help with the priority queue

2. To store all the processes, I use an ArrayList

3. When a process is retrieved from an ArrayList, it is added to the PriorityQueue, so I use
PriorityQueue
