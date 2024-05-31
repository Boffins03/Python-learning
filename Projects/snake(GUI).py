import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
ROWS = 20
COLS = 20
SQUARE_SIZE = WIDTH // ROWS

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Directional vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Cube:
    def __init__(self, pos, color=GREEN):
        self.pos = pos
        self.color = color

    def draw(self, surface):
        x, y = self.pos
        pygame.draw.rect(surface, self.color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


class Snake:
    def __init__(self, pos):
        self.body = [Cube(pos)]
        self.direction = RIGHT
        self.turns = {}

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.direction = LEFT
                elif keys[pygame.K_RIGHT]:
                    self.direction = RIGHT
                elif keys[pygame.K_UP]:
                    self.direction = UP
                elif keys[pygame.K_DOWN]:
                    self.direction = DOWN

        for i, cube in enumerate(self.body):
            pos = cube.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                cube.pos = (cube.pos[0] + turn[0], cube.pos[1] + turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                cube.pos = (cube.pos[0] + self.direction[0], cube.pos[1] + self.direction[1])

    def reset(self):
        self.body = [Cube((COLS // 2, ROWS // 2))]
        self.direction = RIGHT
        self.turns = {}

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.pos[0] - self.body[-2].pos[0], tail.pos[1] - self.body[-2].pos[1]
        if dx == 0:
            if dy == 1:
                self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
            elif dy == -1:
                self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))
        elif dy == 0:
            if dx == 1:
                self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
            elif dx == -1:
                self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))

    def draw(self, surface):
        for cube in self.body:
            cube.draw(surface)


def random_snack(snake):
    while True:
        x = random.randrange(COLS)
        y = random.randrange(ROWS)
        if (x, y) not in snake.body:
            return (x, y)


def draw_grid(surface):
    for i in range(ROWS):
        pygame.draw.line(surface, WHITE, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
        pygame.draw.line(surface, WHITE, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT))


def redraw_window(surface, snake, snack):
    surface.fill(BLACK)
    draw_grid(surface)
    snake.draw(surface)
    snack.draw(surface)
    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake((COLS // 2, ROWS // 2))
    snack = Cube(random_snack(snake), color=RED)

    run = True
    while run:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.add_cube()
            snack = Cube(random_snack(snake), color=RED)

        for i in range(1, len(snake.body)):
            if snake.body[i].pos == snake.body[0].pos:
                snake.reset()
                break

        if snake.body[0].pos[0] >= COLS or snake.body[0].pos[0] < 0 or \
                snake.body[0].pos[1] >= ROWS or snake.body[0].pos[1] < 0:
            snake.reset()

        redraw_window(win, snake, snack)

    pygame.quit()


if __name__ == "__main__":
    main()
