import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GAME_WIDTH, GAME_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define Snake class
class Snake:
    def __init__(self):
        self.body = [(GAME_WIDTH // 2, GAME_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        if new_head in self.body or not (0 <= new_head[0] < GAME_WIDTH) or not (0 <= new_head[1] < GAME_HEIGHT):
            return False  # Game over
        self.body.insert(0, new_head)
        if new_head == food.position:
            self.grow = True
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Define Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return (random.randint(0, GAME_WIDTH - 1), random.randint(0, GAME_HEIGHT - 1))

    def draw(self, surface):
        pygame.draw.rect(surface, FOOD_COLOR, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Initialize game variables
snake = Snake()
food = Food()
score = 0

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Game loop
running = True
game_over = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)
            elif event.key == pygame.K_r:
                if game_over:
                    snake = Snake()
                    food = Food()
                    score = 0
                    game_over = False

    # Game logic
    if not game_over:
        game_over = not snake.move()
        if snake.body[0] == food.position:
            food.position = food.randomize_position()
            score += 1

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    snake.draw(screen)
    food.draw(screen)
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press 'R' to restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    else:
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)  # Control game speed

# Quit Pygame
pygame.quit()
