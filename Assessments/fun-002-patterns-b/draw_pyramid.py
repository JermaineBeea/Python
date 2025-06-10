# TODO: Complete the required shape below with reference to the unittests
def draw_pyramid(height:int)->None:
    """
    Draws a centered pyramid pattern of asterisks (*) with the given height.
    
    Parameters:
        height (int): The height of the pyramid. Must be a positive integer.
        
    Returns:
        None: Prints the pyramid pattern directly to console.
        
    """
    
    for row in range(height):
        space = ' ' * (height - (row + 1))
        
        print(space + '*' * (2 * row + 1))


