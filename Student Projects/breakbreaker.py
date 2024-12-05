import pygame  
import random  

pygame.init()  
 
WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Breakout Game")  


WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  

  
PADDLE_WIDTH = 100  
PADDLE_HEIGHT = 10  
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2  
paddle_y = HEIGHT - 30  
paddle_speed = 10  


BALL_RADIUS = 10  
ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)  
ball_y = HEIGHT - 50  
ball_speed_x = random.choice([-5, 5])  
ball_speed_y = -5  

  
BRICK_WIDTH = 75  
BRICK_HEIGHT = 20  
bricks = []  

for i in range(7):  
    for j in range(5):  
        bricks.append(pygame.Rect(i * (BRICK_WIDTH + 10) + 50, j * (BRICK_HEIGHT + 10) + 50, BRICK_WIDTH, BRICK_HEIGHT))  


running = True  
clock = pygame.time.Clock()  
score = 0  

 
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  

  
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT] and paddle_x > 0:  
        paddle_x -= paddle_speed  
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:  
        paddle_x += paddle_speed  

  
    ball_x += ball_speed_x  
    ball_y += ball_speed_y  

  
    if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:  
        ball_speed_x *= -1  
    if ball_y <= BALL_RADIUS:  
        ball_speed_y *= -1  
    if ball_y >= HEIGHT:  
        running = False  

 
    if (paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT) and (paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH):  
        ball_speed_y *= -1  
        ball_y = paddle_y - BALL_RADIUS   


    for brick in bricks[:]:  
        if brick.collidepoint(ball_x, ball_y):  
            ball_speed_y *= -1  
            bricks.remove(brick)  
            score += 1  
            break  

  
    screen.fill(BLACK)  
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)  

    for brick in bricks:  
        pygame.draw.rect(screen, GREEN, brick)  

  
    font = pygame.font.Font(None, 36)  
    score_text = font.render(f"Score: {score}", True, WHITE)  
    screen.blit(score_text, (10, 10))  

    pygame.display.flip()  
    clock.tick(60) 

pygame.quit()