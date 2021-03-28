import java.util.Scanner;

public class HailstoneSequence {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        int n = Integer.parseInt(sc.nextLine());
        int steps = 0;
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
                steps++;
            } else {
                n = 3 * n + 1;
                steps++;
            }
            System.out.println((n % 2 == 0) ? n + " is even, so divide by 2: " + (n / 2) : n + " is odd, so calculate 3n + 1: " + (3 * n + 1));
        }
        System.out.println("The hailstone sequence took " + steps + " steps to reach 1.");
    }
}
