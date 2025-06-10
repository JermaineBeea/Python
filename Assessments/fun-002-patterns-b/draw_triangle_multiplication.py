# TODO: Complete the required shape below with reference to the unittests
def draw_triangle_multiplication(height:int)->None:
    """
    Draws a multiplication triangle where each row shows products of the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the multiplication triangle pattern directly to console.
        
    """
    
    for row in range(height):
        print(' '.join(str((row  + 1) * (num + 1)) for num in range(row + 1)), '')


