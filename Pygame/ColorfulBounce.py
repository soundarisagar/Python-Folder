import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHT_BLUE = pygame.Color('lightblue')
DARK_BLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
ORANGE = pygame.Color('orange')
MAGENTA = pygame.Color('magenta')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self, color):
        self.image.fill(random.choice([YELLOW, ORANGE, MAGENTA, WHITE]))

def change_background_color():
    global background_color
    bg_color = random.choice([BLUE, LIGHT_BLUE, DARK_BLUE])

all_sprites = pygame.sprite.Group()
sp1 = Sprite(BLUE, 50, 50)
sp1.rect.x = random.randint(0, 450)
sp1.rect.y = random.randint(0, 450)
all_sprites.add(sp1)
screen = pygame.display.set_mode((500, 500))
background_color = BLUE
screen.fill(background_color)
exit_program = False
clock = pygame.time.Clock()

while not exit_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color(random.choice([YELLOW, ORANGE, MAGENTA, WHITE]))
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites.update()
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()    