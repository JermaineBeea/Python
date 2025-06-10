def draw_triangle_reversed(height):

    for row in range(height):
        
        print(' '.join([str(row + 1)] * (height - row)), '')
    
