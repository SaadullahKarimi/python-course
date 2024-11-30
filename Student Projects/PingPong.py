# Import the necessary libraries  
import pygame  
import sys  

# Initialize Pygame  
pygame.init()  

# Constants for the game settings  
WIDTH, HEIGHT = 800, 600  # Screen dimensions  
WHITE = (255, 255, 255)    # Color white in RGB  
BLACK = (0, 0, 0)          # Color black in RGB  
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100  # Paddle dimensions  
BALL_SIZE = 10             # Ball size  
PADDLE_SPEED = 10          # Paddle movement speed  
BALL_SPEED_X = 5           # Initial horizontal ball speed  
BALL_SPEED_Y = 5           # Initial vertical ball speed  
WINNING_SCORE = 5          # Score needed to win  

# Set up the display  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Ping Pong Game")  # Title of the game window  

# Initialize font for displaying scores  
font = pygame.font.Font(None, 74)  
button_font = pygame.font.Font(None, 36)  # Font for the restart button  

# Create paddles and ball  
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)  

# Initialize ball velocity  
ball_velocity_x = BALL_SPEED_X  
ball_velocity_y = BALL_SPEED_Y  

# Initialize scores for both players  
left_score = 0  
right_score = 0  

def reset_game():  
    """Reset the game state."""  
    global left_score, right_score, ball, ball_velocity_x, ball_velocity_y  
    left_score = 0  
    right_score = 0  
    ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset ball position  
    ball.y = HEIGHT // 2 - BALL_SIZE // 2  
    ball_velocity_x = BALL_SPEED_X  
    ball_velocity_y = BALL_SPEED_Y  

# Main game loop  
while True:  
    for event in pygame.event.get():  # Check for events  
        if event.type == pygame.QUIT:  # If the window is closed  
            pygame.quit()              # Quit Pygame  
            sys.exit()                 # Exit the program  

    # Get the current state of all keys  
    keys = pygame.key.get_pressed()  

    # Move the paddles based on key presses  
    if keys[pygame.K_w] and left_paddle.top > 0:  # Move left paddle up  
        left_paddle.y -= PADDLE_SPEED  
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:  # Move left paddle down  
        left_paddle.y += PADDLE_SPEED  
    if keys[pygame.K_UP] and right_paddle.top > 0:  # Move right paddle up  
        right_paddle.y -= PADDLE_SPEED  
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:  # Move right paddle down  
        right_paddle.y += PADDLE_SPEED  

    # Move the ball  
    ball.x += ball_velocity_x  
    ball.y += ball_velocity_y  

    # Check for ball collision with top and bottom of the screen  
    if ball.top <= 0 or ball.bottom >= HEIGHT:  
        ball_velocity_y = -ball_velocity_y  # Reverse vertical direction  

    # Check for ball collision with paddles  
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):  
        ball_velocity_x = -ball_velocity_x  # Reverse horizontal direction  

    # Reset ball if it goes past paddles  
    if ball.left <= 0:  # If the ball goes past the left paddle  
        right_score += 1  # Right player scores  
        ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset ball position  
        ball.y = HEIGHT // 2 - BALL_SIZE // 2  
        ball_velocity_x = BALL_SPEED_X  # Reset direction to the right  

    if ball.right >= WIDTH:  # If the ball goes past the right paddle  
        left_score += 1  # Left player scores  
        ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset ball position  
        ball.y = HEIGHT // 2 - BALL_SIZE // 2  
        ball_velocity_x = -BALL_SPEED_X  # Reset direction to the left  

    # Clear the screen  
    screen.fill(BLACK)  

    # Draw paddles and ball  
    pygame.draw.rect(screen, "blue", left_paddle)  
    pygame.draw.rect(screen, "blue", right_paddle)  
    pygame.draw.ellipse(screen, WHITE, ball)  

    # Render scores  
    left_score_text = font.render(str(left_score), True, WHITE)  
    right_score_text = font.render(str(right_score), True, WHITE)  
    screen.blit(left_score_text, (WIDTH // 4, 20))  # Position for left score  
    screen.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width(), 20))  # Position for right score  

    # Check for a winner  
    if left_score >= WINNING_SCORE:  # If left player reaches winning score  
        winner_text = font.render("Left Player Wins!", True, WHITE)  
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))  
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 10, 200, 50)  # Button rectangle  
        pygame.draw.rect(screen, WHITE, restart_button)  # Draw button  
        button_text = button_font.render("Restart Game", True, BLACK)  # Button text  
        screen.blit(button_text, (restart_button.x + 20, restart_button.y + 10))  # Position button text  

        # Check for mouse click on the restart button  
        mouse_pos = pygame.mouse.get_pos()  
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1 and restart_button.collidepoint(mouse_pos):  # Left click on button  
                reset_game()  # Restart the game  

    elif right_score >= WINNING_SCORE:  # If right player reaches winning score  
        winner_text = font.render("Right Player Wins!", True, WHITE)  
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))  
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 10, 200, 50)  # Button rectangle  
        pygame.draw.rect(screen, WHITE, restart_button)  # Draw button  
        button_text = button_font.render("Restart Game", True, BLACK)  # Button text  
        screen.blit(button_text, (restart_button.x + 20, restart_button.y + 10))  # Position button text  

        # Check for mouse click on the restart button  
        mouse_pos = pygame.mouse.get_pos()  
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1 and restart_button.collidepoint(mouse_pos):  # Left click on button  
                reset_game()  # Restart the game  

    # Update the display  
    pygame.display.flip()  

    # Cap the frame rate  
    pygame.time.Clock().tick(60)