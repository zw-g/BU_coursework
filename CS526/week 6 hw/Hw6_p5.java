import java.io.*;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

// Adjascency List representation in Java
class Hw6_p5 {

  /*
  - The name of the method must be allFollows.
  - The method must receive two arguments: a person X and an adjacency list adjList
  - Then, the method must print on the screen all people X directly follows and all people X
    indirectly follows. For example, if D and the above adjacency list are passed as arguments, your output must be:

    D directly follows {B, C, E} 
    D indirectly follows {F, G}
  */
  static ArrayList<Node> adjList = new ArrayList<Node>();
  static ArrayList<String> checker = new ArrayList<String>();
  static ArrayList<String> indirectly = new ArrayList<String>();

  static String indirectFollow(String X, ArrayList<Node> adjList){
    Iterator itr=adjList.iterator();
    while(itr.hasNext()){
      Node nd=(Node)itr.next();
      if (checker.contains(nd.X)){
        for(int i = 0; i<nd.Y.size(); i++){
          if(!checker.contains(nd.Y.get(i))){
            checker.add(nd.Y.get(i));
            //System.out.println(nd.Y.get(i));
            indirectly.add(indirectFollow(nd.Y.get(i), adjList));
            return nd.Y.get(i);
          }
        }
      }
    }
    return "end";
  }

  static void allFollows(String X, ArrayList<Node> adjList){
    Iterator itr=adjList.iterator();

    //print driectly follow first
    if(checker.size() == 0){
      //traverse elements of ArrayList object  
      while(itr.hasNext()){  
        Node nd=(Node)itr.next();
        //System.out.println(nd.X);
        //System.out.println(X);
        if (nd.X.equalsIgnoreCase(X)){
          System.out.print(nd.X+" directly follows {");
          if(nd.Y.size() == 0)
            System.out.println("}");
          for(int i = 0; i<nd.Y.size(); i++){
            checker.add(nd.Y.get(i));
            System.out.print(nd.Y.get(i));
            if (i != nd.Y.size()-1){
              System.out.print(", ");
            }
            else{
              System.out.println("}");
            }
          }
        }
        //System.out.println(nd.X+": "+nd.Y);
      }
    }

    indirectly.add(indirectFollow(X, adjList));

    //print indirectly follow first
    System.out.print(X+" indirectly follows {");
    for(int i = 0; i<indirectly.size(); i++){
      if (!indirectly.get(i).equalsIgnoreCase("end")){
        System.out.print(indirectly.get(i));
      }
      if (i != indirectly.size()-1 && !indirectly.get(i).equalsIgnoreCase("end")){
        System.out.print(", ");
      }
      if (i == indirectly.size()-1){
        System.out.println("}\n");
      }
    }
    indirectly.clear();
    checker.clear();
  }

  static ArrayList<Node> LoadFile(String txtFileName) throws Exception{
    //read file
    File file = new File(txtFileName + ".txt");
    Scanner sc = new Scanner(file);
    
    //this is the adjList that will store
    ArrayList<String> tempY = new ArrayList<String>();
    String line;

    int count = 0;
    while (sc.hasNextLine()){
      tempY.clear();
      line = sc.nextLine();
      //System.out.println(line);
      String string[] = line.split(", ");
      //System.out.println(string[0]);
      for(int i = 1; i < string.length; i++)
        tempY.add(string[i]);
      //System.out.println(tempY);
      adjList.add(new Node(string[0], tempY));
      count ++;
    }
    sc.close();
    return adjList;
    /*
    Iterator itr=adjList.iterator();  

    //traverse elements of ArrayList object  
    while(itr.hasNext()){  
      Node nd=(Node)itr.next();  
      System.out.println(nd.X+": "+nd.Y);
    }
    */
  }

  public static void main(String[] args) throws Exception{
    checker.clear();

    //load the file input the name of the file
    adjList = LoadFile("follows_input");

    allFollows("A", adjList);
    allFollows("B", adjList);
    allFollows("C", adjList);
    allFollows("D", adjList);
    allFollows("E", adjList);
    allFollows("F", adjList);
    allFollows("G", adjList);
  }
}

//store the node X and the arraylist Y
class Node{
  public String X;
  public ArrayList<String> Y = new ArrayList<String>();
  Node(String X, ArrayList<String> tempY){
    this.X = X;
    this.Y = (ArrayList)tempY.clone();
  }
  public String getx(){
    return X;
  }
  public ArrayList<String> gety(){
    return Y;
  }
}