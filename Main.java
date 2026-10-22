import java.util.Scanner;

public class Main {

    public static void main (String [] args) {

        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your First Number: ");
        double num1 = input.nextDouble();

        input.nextLine();

        System.out.print("Enter your Desired Operation (+ ,- ,* , /): ");
        String opt = input.nextLine();

        System.out.print("Enter your Second Number: ");
        double num2 = input.nextDouble();

        if (opt.equals("+")) {

                System.out.println("Answer: ");
                System.out.print(num1 + num2);
                
        } else if (opt.equals("-")) {

                System.out.println("Answer: ");
                System.out.print(num1 - num2);

        } else if (opt.equals("*")) {

                System.out.println("Answer: ");
                System.out.print(num1 * num2);

        } else if (opt.equals("/")) {

                if (num2 == 0) {

                  System.out.println("Syntax Error. Cannot Divide by Zero");
                        } else {
                
                System.out.println("Answer: ");
                System.out.print(num1 / num2); }

        } else {

                System.out.println("Plz select an operation from the given list");
        }
    }
}
