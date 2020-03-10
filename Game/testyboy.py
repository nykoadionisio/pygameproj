import pygame

#Setting Up Window
pygame.init()
win = pygame.display.set_mode((1440, 900))
pygame.display.set_caption("First Game")

#Sprites
walkRight = [pygame.image.load('WizardR0.png'),pygame.image.load('WizardR1.png'),pygame.image.load('WizardR2.png'),pygame.image.load('WizardR3.png'),pygame.image.load('WizardR4.png'),pygame.image.load('WizardR5.png'),pygame.image.load('WizardR6.png'),pygame.image.load('WizardR7.png'),pygame.image.load('WizardR8.png')]
walkLeft = [pygame.image.load('WizardL0.png'),pygame.image.load('WizardL1.png'),pygame.image.load('WizardL2.png'),pygame.image.load('WizardL3.png'),pygame.image.load('WizardL4.png'),pygame.image.load('WizardL5.png'),pygame.image.load('WizardL6.png'),pygame.image.load('WizardL7.png'),pygame.image.load('WizardL8.png')]
char = pygame.image.load('WizardR0.png')
backdrop = pygame.image.load('Backdrop0.png')

#Ingame Clock
clock = pygame.time.Clock()

#Class MC
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

#Direction of Character
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 1], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


#Projectiles
class maBu(object):
    def __init__(self, x, y, radius, color, facing, cooldown = 200):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#Drawing The Game
def redrawGameWindow():
    win.blit(backdrop, (0, 0))
    mc.draw(win)
    for magic in magicShot:
        magic.draw(win)

    pygame.display.update()

#Main Loop
mc = player(50, 675, 64, 64)
shootLoop = 0
shootTime = 0
magicShot = []
run = True
while run:
        clock.tick(27)

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for magic in magicShot:
            if magic.x < 1440 and magic.x > 0:
                magic.x += magic.vel

            else:
                magicShot.pop(magicShot.index(magic))


        keys = pygame.key.get_pressed()
        if mc.left:
            facing = -1

        else:
            facing = 1
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if len(magicShot) < 20:
                magicShot.append(maBu(round(mc.x + mc.width //2), round(mc.y + mc.height //2), 6, (75, 0, 130), facing))


            shootLoop = 1

        if keys[pygame.K_LEFT] and mc.x > mc.vel:
            mc.x -= mc.vel
            mc.right = False
            mc.left = True
            mc.standing = False

        elif keys[pygame.K_RIGHT] and mc.x < 1440 - mc.width - mc.vel:
            mc.x += mc.vel
            mc.right = True
            mc.left = False
            mc.standing = False

        else:
            mc.standing = True
            mc.walkCount = 0

        if not(mc.isJump):
            if keys[pygame.K_UP]:
                mc.isJump = True
                mc.right = False
                mc.left = False
                mc.walkCount = 0

        else:
            if mc.jumpCount >= -10:
                neg = 0.5
                if mc.jumpCount < 0:
                    neg = -0.5
                mc.y -= (mc.jumpCount ** 2) * 0.5 * neg
                mc.jumpCount -= 1

            else:
                mc.isJump = False
                mc.jumpCount = 10

        redrawGameWindow()

pygame.quit()