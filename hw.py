import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("PYGAME CHANGING COLOR")
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def change_color(self, new_color):
        self.image.fill(new_color)
sprite1 = MySprite(RED, 50, 100)
sprite2 = MySprite(BLUE, 200, 100)
all_sprites = pygame.sprite.Group(sprite1, sprite2)
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color(GREEN)
            sprite2.change_color(RED)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()