import pygame, sys, random

pygame.init()

game_over = False
score = 0

font = pygame.font.SysFont("Bauhaus 93", 58)

sw = 800
sh = 700

bg_image = pygame.image.load("background.png")
ground_image = pygame.image.load("ground.png")
restart_btn_image = pygame.image.load("restart_button.png")

pipe_freq = 1500
last_pipe = pygame.time.get_ticks() - pipe_freq

pass_pipe = False

pipe_gap = 150

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("flappy bird")
screen.fill("white")

pygame.display.update()

def draw_txt(x,y):
    txt = font.render("score:" + str(score), True, "white")
    screen.blit(txt, (x, y))

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

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = 1
                self.vel = -10
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = 0

            self.image = pygame.transform.rotate(self.images[self.index],-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)


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
    def update(self):
        self.rect.x -= 6
        if self.rect.right < 0:
            self.kill()

flappy = Bird(100, 250)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

move_ground = 0
speed = 5

flying = False

pipe_group = pygame.sprite.Group()

class Button():
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action
    
button = Button(restart_btn_image, sw/2 - 50, sh/2)

def reset():
    flappy.rect.x = 100
    flappy.rect.y = 250
    pipe_group.empty()
    score = 0
    return score

while True:
    screen.blit(bg_image, (0,0))

    draw_txt(sw - 200, 25)

    bird_group.draw(screen)
    pipe_group.draw(screen)

    bird_group.update()
    pipe_group.update()

    screen.blit(ground_image, (move_ground,580))
    move_ground -= speed

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False)\
    or flappy.rect.top < 0:
        game_over = True

    if game_over == True:
        move_ground = 0
        if button.draw():
            game_over = False
            score = reset()

    if abs(move_ground) > 35:
        move_ground = 0
    
    if flying == True and game_over == False:
        time_now = pygame.time.get_ticks()

        if time_now - last_pipe > pipe_freq:
            pipe_height = random.randint(-100, 100)
            top_pipe = Pipe(1, sw, sh/2 - (pipe_gap/2) + pipe_height)
            bottom_pipe = Pipe(-1, sw, sh/2 + (pipe_gap/2) + pipe_height)
            pipe_group.add(top_pipe, bottom_pipe)
            last_pipe = time_now
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
        and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
        and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
            



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True


    pygame.display.update()
