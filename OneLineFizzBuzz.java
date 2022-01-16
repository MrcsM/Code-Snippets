// Basic FizzBuzz, div by 15 = FizzBuzz, div by 3 = Fizz, div by 5 = Buzz, rest = number
// idk i was more impressed by the fact i did this with 1 line

public class OneLineFizzBuzz {
    public static void main(String[] arg) {
        for (int i = 1; i <= 100; i++) System.out.println((i % 15 == 0 ? "FizzBuzz" : (i % 3 == 0 ? "Fizz" : (i % 5 == 0 ? "Buzz" : i))));
    }
}
