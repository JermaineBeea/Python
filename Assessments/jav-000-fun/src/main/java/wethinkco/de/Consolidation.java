package wethinkco.de;
import java.util.ArrayList;
// import java.util.Arrays;
import java.util.List;
public class Consolidation {

    private static String fizzOnce(int number){
        if(number % 15 == 0) return "FizzBuzz";
        if(number % 5 == 0) return "Buzz";
        if(number % 3 == 0) return "Fizz";
        return String.valueOf(number);
    }

    public static void main(String[] args) {
        System.out.println(fibonacciSequence(7));
        System.out.println(fizzBuzz(15));
        System.out.println(drawTriangle(6));
        System.out.println(isPalindrome("hello"));
        System.out.println(factorial(5));
    }

    public static List<String> fizzBuzz(int n) {
    
        List<String> result = new ArrayList<>();
        for(int indx = 0; indx < n; indx ++){
            result.add(fizzOnce(indx + 1));
        }
        return result;
    }

    public static String fibonacciSequence(int num){
        StringBuilder result = new StringBuilder();
        if(num <= 0) return result.toString();
        int a = 0; int b = 1;
        result.append(a);
        if(num == 1) return result.toString();
        result.append(" ").append(b);
        for(int indx = 2; indx < num; indx ++){
            int next = a + b;
            result.append(" ").append(next);
            a = b;
            b = next;
        }
        return result.toString();
    }

    public static String calculate(int a, int b, String operator){
        return switch(operator){
            case "+" -> String.valueOf(a + b);
            case "-" -> String.valueOf(a - b);
            case "%" -> String.valueOf(a % b);
            case "/" -> String.valueOf(a / b);
            default -> "";
        };
    }

    public static String drawTriangle(int num){
        StringBuilder result = new StringBuilder();
        for(int indx = 0; indx < num; indx ++){
            result.append("*".repeat(indx + 1));
        }   
        return result.toString();
    }

    public static boolean isPalindrome(String str){
        StringBuilder result = new StringBuilder();
        str.toLowerCase().chars().filter(Character::isAlphabetic).forEach(k -> result.append((char) k));
        return result.toString().contentEquals(new StringBuilder(result).reverse().toString());
    }

    public static long factorial(int num){
        int result = 1;
        for(int indx = 0; indx < num; indx++){
            result *= indx + 1;
        }
        return (long) result;
    }
}
