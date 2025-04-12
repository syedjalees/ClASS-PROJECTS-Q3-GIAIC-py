from graphics import Canvas 
import time

# Constants for canvas dimensions and cell sizes
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get the current mouse position to determine which cells to erase
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate the bounds of the eraser based on the mouse position
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find all objects that overlap with the eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Change the color of all overlapping objects (except the eraser itself) to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

def main():
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate how many rows and columns fit in the canvas
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Draw the grid of blue cells on the canvas
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Create a blue rectangle for each cell
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    # Wait for the user to click on the canvas to start erasing
    canvas.wait_for_click()
    
    # Get the coordinates of the first click (where the eraser will start)
    last_click_x, last_click_y = canvas.get_last_click()
    
    # Create the eraser as a pink rectangle
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser with the mouse and erase cells in contact with it
    while True:
        # Get the current mouse position and move the eraser
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase objects under the eraser
        erase_objects(canvas, eraser)
        
        # Pause for a short time to make the movement smooth
        time.sleep(0.05)

if __name__ == '__main__':
    main()
