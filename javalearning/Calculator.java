package javalearning;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        // user input
        Scanner sc = new Scanner(System.in);

        while (true) {
            // first number
            System.out.println("Enter the first number: ");
            int first_number = sc.nextInt();

            // second number
            System.out.println("Enter the second number: ");
            int second_number = sc.nextInt();

            // operation choice
            System.out.println("Choose an operation (add, subtract, multiply or division): ");
            String operation = sc.next();

            // perform the operation
            if (operation.equals("add")) {
                int add = first_number + second_number;
                System.out.println(first_number + " + " + second_number + " = " + add);
            } else if (operation.equals("subtract")) {
                int subtract = first_number - second_number;
                System.out.println(first_number + " - " + second_number + " = " + subtract);
            } else if (operation.equals("multiply")) {
                int multiply = first_number * second_number;
                System.out.println(first_number + " * " + second_number + " = " + multiply);
            } else if (operation.equals("division")) {
                if (second_number == 0) {
                    System.out.println("Error: Division by zero is not allowed.");
                } else {
                    int division = first_number / second_number;
                    System.out.println(first_number + " / " + second_number + " = " + division);
                }
            } else {
                System.out.println("Error: Select a valid operation.");
            }

            // exit or replay menu
            System.out.println("Choose an option:");
            System.out.println("[1] Make another operation");
            System.out.println("[2] Exit");

            int replay_menu = sc.nextInt();

            if (replay_menu == 2) {
                System.out.println("Thank you and see you soon!");
                sc.close();
                System.exit(0);
            }
        }
    }
}