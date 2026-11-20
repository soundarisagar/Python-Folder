import pygame

def main():
    pygame.init()
    screen_width, screen_height = 400, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Colour Changing Sprite")

    colours = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white"),
    }
    current_colour = colours["white"]
    x,y = 30, 30
    width, height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            x += 5
        if pressed_keys[pygame.K_UP]:
            y -= 5
        if pressed_keys[pygame.K_DOWN]:
            y += 5
        x = min (max(x, 0), screen_width - width)
        y = min (max(y, 0), screen_height - height)

        if x == 0:
            current_colour = colours["red"]
        elif x == screen_width - width:
            current_colour = colours["yellow"]
        elif x == screen_width // 2 - width // 2:
            current_colour = colours["green"]
        elif y == 0:
            current_colour = colours["red"]
        elif y == screen_height - height:
            current_colour = colours["blue"]
        else:
            current_colour = colours["white"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_colour, pygame.Rect(x, y, width, height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit

if __name__ == "__main__":
    main()    
