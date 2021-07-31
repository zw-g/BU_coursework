
import java.io.IOException;
import java.io.File;
import java.util.Scanner;

public class Hw1_p2 {
	public static void findByMake(Car[] cars, String make) {
		// implement this method

		//initial loop and check
		int i = 0;
		boolean check = true;

		//check if in x
		while (i < cars.length) {
			String tempMake = cars[i].getMake();
			if (tempMake.equals(make)) {
				cars[i].display();
				check = false;
			}
			i = i + 1;
		}

		//if not in x print this
		if (check) {
			System.out.println("there is no car with the given: " + make);
		}
	}
	
	public static void newerThan(Car[] cars, int year) {
		// implement this method

		//initial loop and check
		int i = 0;
		boolean check = true;

		//check if in x
		while (i < cars.length) {
			int tempYear = cars[i].getYear();
			if (tempYear > year) {
				cars[i].display();
				check = false;
			}
			i = i + 1;
		}

		//if not in x print this
		if (check) {
			System.out.println("there is no car newer than the given: " + year);
		}
	}
	
	public static void main(String[] args) throws IOException {
		// complete this part

		// create an array of Car objects, cars, of size 10
		Car[] cars = new Car[10];

		// read input file and store 10 car Objects in the array
		File myObj = new File("car_input.txt");
		Scanner myReader = new Scanner(myObj);
		int count = 0;
		while (myReader.hasNextLine()) {
			String data = myReader.nextLine().replaceAll(",", "");
			String[] temStrArr = data.split(" ", 3);
			int[] temIntArr = new int[2];
			temIntArr[0] = Integer.parseInt(temStrArr[1]);
			temIntArr[1] = Integer.parseInt(temStrArr[2]);
			cars[count] = new Car(temStrArr[0],  temIntArr[0], temIntArr[1]);
			count = count + 1;
		}
		myReader.close();

		//print all the cars
		System.out.println("\nAll cars:");
		for (int i=0; i<cars.length; i++) {
			cars[i].display();
		}

		String make = "Honda";
		int year = 2017;
		
		System.out.println("\nAll cars made by " + make);
		findByMake(cars, make);

		System.out.println("\nAll cars made after " + year);
		newerThan(cars, year);
	}
}

class Car{
	public String Make;
	public int Year;
	public int Price;
	public Car(String m, int p, int y){
		Make = m;
		Year = y;
		Price = p;
	}

	public void display() 
    {
    	int makeLen = 7 - Make.length();
        System.out.print("Make = " + Make);
        for (int i = 0; i < makeLen; i++)
        	System.out.print(" ");
        System.out.println(" Year = " + Year + "    Price = " + Price);
    } 

    public String getMake(){
    	return Make;
    }
    public Integer getYear(){
    	return Year;
    }
}


