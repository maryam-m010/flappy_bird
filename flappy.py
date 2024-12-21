import pygame, sys

pygame.init()

game_over = False

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
        self.clicked = 0

    def update(self):
        self.index += 1

        if flying == True:
            self.vel += 0.5
            print(self.vel)

            if self.vel > 8:
                self.vel = 8

            if self.rect.bottom < 580:
                self.rect.y += self.vel

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = 1
                self.vel = -10
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = 0

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, x, y):
        pygame.sprite.Sprite.__init__(self) #superior class: properties can be inherited from it by child class
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y]
        elif pos == -1:
            self.rect.topleft = [x,y]

flappy = Bird(100,100)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

move_ground = 0
speed = 5

flying = False

while True:
    screen.blit(bg_image, (0,0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground_image, (move_ground,580))
    move_ground -= speed
    if abs(move_ground) > 35:
        move_ground = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()
