# TODO: Complete the required shape below with reference to the unittests
def draw_triangle(height:int)->None:
    """
    Draws a number triangle where each row contains sequential numbers from 1 to the row number.
    
    Parameters:
        height (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to console.
    
        
    """
    
    for row in range(height):

        print(' '.join(str(num + 1) for num in range(row + 1)), '')


