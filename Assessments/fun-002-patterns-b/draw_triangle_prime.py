# TODO: Complete the required shape below with reference to the unittests
def draw_triangle_prime(height:int)->None:
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the prime number triangle pattern directly to console.
        
    """
    
    def is_prime(number):

        if number == 2:
            return True
        
        if number == 1 or number % 2 == 0:
            return False
        
        current_odd = 3

        while current_odd < number:
            if number % current_odd == 0:
                return False
            
            current_odd += 2
        
        return True
    
    def prime_list(start, end):

        if end == 0:
                return [2]
        
        p_list = [2, 3]

        indx = 0
        current_odd = 5

        while indx < end:
                
            if is_prime(current_odd):
                p_list.append(current_odd)
                indx += 1
            
            current_odd += 2
        
        return p_list[start: end + 1]
    
    def arithmetic_sum(number):
        return int(number * (number + 1) / 2)
    

    for row in range(height):

        start_indx = arithmetic_sum(row)
        end_indx = start_indx + row

        print(' '.join(str(num) for num in prime_list(start_indx, end_indx)), '')









