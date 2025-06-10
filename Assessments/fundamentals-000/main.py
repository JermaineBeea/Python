import prime_numbers
import sequences

if __name__ == '__main__':
    
    print(prime_numbers.is_prime(24))
    print(prime_numbers.generate_primes(15))
    print(prime_numbers.sum_all_primes(15))
    
    print(sequences.generate_fibonacci(15))
    print(sequences.generate_squares(15))
    print(sequences.generate_cubes(15))
    print(sequences.is_in_fibonacci_sequence(15))
    