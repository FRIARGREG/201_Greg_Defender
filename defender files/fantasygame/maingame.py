##############################################################################
## THIS IS THE MAIN CODE FOR GREG'S DEFENDER
##############################################################################
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (0, 0, 255)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
     
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    drawstuf()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()

##############################################################################
## THIS IS THE SUPPORTING CODE FOR THE MAIN LOOP ABOVE
##############################################################################

## I MOVED THE DRAWING OF THINGS TO THIS FUNCTION TO KEEP THE GAME LOOP CLEAN
def drawstuff():
     
    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
 
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
 
    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
 
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
 
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)
 
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
 
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("My text", True, BLACK)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()