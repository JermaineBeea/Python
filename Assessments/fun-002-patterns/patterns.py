
# TODO: return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape()-> str:
    
    valid_shapes = 'square', 'triangle', 'triangle_reversed', 'triangle_multiplication', 'pyramid', 'triangle_prime'
    while True:
        shape = input('Please enter shape to draw: ').lower().strip()
        if shape in valid_shapes:
            return shape
        else:
            print("Invalid shape. Please enter a valid shape.")


# TODO: return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height()->int:
    
    while True:

        try:
            height = input('Please enter height: ')
            height = int(height)
            if 1<= height <= 80:
                return height
            else:
                print('Please enter valid number')
        except ValueError:
            print('Please enter valid number')


# TODO: Complete the required shapes below
#       with reference to the unittests
def draw_square(height:int)->None:
    
    """
    Draws a square pattern of asterisks (*) with the given height and width.
    
    Parameters:
        height (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the square pattern directly to console.
        
    """
    for _ in range(height):
        print('*'*height)


def draw_pyramid(height:int)->None:
    
    """
    Draws a centered pyramid pattern of asterisks (*) with the given height.
    
    Parameters:
        height (int): The height of the pyramid. Must be a positive integer.
        
    Returns:
        None: Prints the pyramid pattern directly to console.
        
    """
    
    pass

def draw_triangle(height:int)->None:
    
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    
    for n in range(height, 0, -1):
        print(' '.join([str(height - n + 1)*n][0]))


def draw_triangle_reversed(height:int)->None:
    
    """
    Draw an inverted number triangle where each row begins with its position number, 
    with the top row having the most repeated numbers and each row below having one fewer repetition.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the inverted triangle pattern directly to console.
        

    """
    
    for n in range(height, 0, -1):
        print(' '.join([str(height - n + 1)*n][0]))



def draw_triangle_multiplication(height:int)->None:
    
    """
    Draws a multiplication triangle where each row shows products of the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the multiplication triangle pattern directly to console.
        
    """
    
    for n in range(1, height + 1):
        print(*[str(n*x) for x in range(1, n + 1)])



def draw_triangle_prime(height:int)->None:
    
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the prime number triangle pattern directly to console.
        
    """
    
    def is_prime(num):
        if num ==1 or num == 0 or (num % 2 == 0):
            return False
        else:
            for n in range(2, num):
                if num % n == 0:
                    return False
        return True

    def primes_list(start_pos, end_pos):
        final = height**2
        if final == 1:
            return [1]
        if final == 2:
            return [2, 3]
        
        list_primes = [2, 3]
        num = 3

        counter = 2
        while counter != final:
            num = num + 2
            if is_prime(num):
                list_primes.append(num)
                counter += 1

        return list_primes[start_pos - 1: end_pos + 1]

    def arithmetic_sum(num):
        return int(num*(num+1)*(1/2))



    for row in range(1,height + 1):
        start = arithmetic_sum(row-1) + 1
        end = start + row - 1
        print(*primes_list(start, end))
            
                
# TODO: add support for other shapes
def draw(shape:str, height:int)->None:
    
    """
    Main drawing function that calls the appropriate shape-specific drawing function
    based on the requested shape type.
    
    Parameters:
        shape (str): The type of shape to draw. Must be one of:
            - "square": A square of asterisks
            - "triangle_reversed": Inverted triangle of repeated row numbers
            - "triangle": Triangle of sequential numbers
            - "triangle_multiplication": Triangle of multiplication products
            - "pyramid": Centered pyramid of asterisks
            - "triangle_prime": Triangle of prime numbers
        height (int): The height of the shape. Must be a positive integer.
        
    Returns:
        None: Prints the requested shape pattern directly to console.
    """
    
    if shape == "pyramid":
        draw_pyramid(height)
    
    if shape == "square":
        draw_square(height)

    if shape == "pyramid":
        draw_pyramid(height)

    if shape == "triangle":
            draw_triangle(height)

    if shape == "triangle_reversed":
        draw_triangle_reversed(height)

    if shape == "triangle_multiplication":
            draw_triangle_multiplication(height)

    if shape == "triangle_prime":
        draw_triangle_prime(height)




# TODO: (standalone function) - Solve Pascal's Triangle
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """

    return ""


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)
    