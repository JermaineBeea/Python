package wethinkco.de;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static wethinkco.de.Consolidation.*;
import java.util.Arrays;
import java.util.List;
public class ConsolidationTest {

    @Test
    public void testFizzBuzz() {
        List<String> expectation = Arrays.asList("1", "2", "Fizz", "4", "Buzz","Fizz", "7", "8", "Fizz", "Buzz","11", "Fizz", "13", "14", "FizzBuzz");
        assertEquals(expectation, fizzBuzz(15));
    }

    @Test
    public void testFibonacciSequence(){
        String expectation = "0 1 1 2 3 5 8";
        assertEquals(expectation, fibonacciSequence(7));
    }



    @Test
    public void testCalculate(){
        assertEquals("7", calculate(2, 5, "+"));
        assertEquals("-3", calculate(2, 5, "-"));
        assertEquals("1", calculate(10, 3, "%"));
        assertEquals("7", calculate(14, 2, "/"));
    }

    @Test
    public void testDrawTriangle(){
        assertEquals("*********************", drawTriangle(6));
    }

    @Test
    public void testIsPalindrome(){
        assertTrue(isPalindrome("racecar"));
        assertTrue(isPalindrome("Racecar"));
        assertFalse(isPalindrome("hello"));
        assertTrue(isPalindrome("a"));
    }

    
    @Test
    public void testFactorial(){
       assertEquals(6, factorial(3));
       assertEquals(120, factorial(5));

    }

    @Test
    public void testFactorial2(){
       assertEquals(24, factorial(4));

    }

}
