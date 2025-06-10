# TODO: Complete the required shape below with reference to the unittests
def draw_square(height:int)->None:
    """
    Draws a square pattern of asterisks (*) with the given height and width.
    
    Parameters:
        height (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the square pattern directly to console.
        
    """
    
    for _ in range(height):
        print('*' * height)