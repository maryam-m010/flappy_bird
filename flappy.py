import pygame, sys

pygame.init()

sw = 800
sh = 700

bg_image = pygame.image.load("background.png")
ground_image = pygame.image.load("ground.png")
restart_btn_image = pygame.image.load("restart_button.png")

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("flappy bird")
screen.fill("white")

pygame.display.update()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__(self)
        self.images = []
        self.index = 0
        for i in range(1,4):
            img = pygame.image.load(f"bird_{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0

    def update(self):
        self.index += 1
        self.image = self.images[self.index]

        if self.index >= len(self.images):
            self.index = 0

        
flappy = Bird(100,100)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

while True:
    screen.blit(bg_image, (0,0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground_image, (0,580))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()