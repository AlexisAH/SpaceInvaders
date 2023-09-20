import pygame
import math
import random
from pygame import mixer

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerLives = 3  # Inicializamos con 3 vidas
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 8 #numero de enemigos en el primer nivel
enemy_destroyed = [False] * num_of_enemies  # registro de enemigos destruidos
nivel_actual = 1
nivel_scores = [10, 20, 30, 40]
enemy_velocidades = [0.4, 0.6, 0.9, 1.2]


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(40)


# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    #verifica si todos los enemigos han sido destruidos
    if all(enemy_destroyed):
        nivel_actual += 1
        if nivel_actual > 4:
            game_over_font = pygame.font.Font('freesansbold.ttf', 64)
            win_text = game_over_font.render("¡Ganaste!", True, (0, 255, 0))
            screen.blit(win_text, (250, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
        if nivel_actual == 2:
            level_text = over_font.render("Nivel 2", True, (0, 255, 0))
            screen.blit(level_text, (300, 250))
            pygame.display.update()
            pygame.time.delay(2000)  #2 segundos antes de continuar

            #restablece los enemigos con nuevas imágenes y velocidades
            num_of_enemies = 9
            enemy_destroyed = [False] * num_of_enemies  #reinicia el seguimiento de enemigos destruidos
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []

            # Crea nuevos enemigos para el nivel actual
            for i in range(num_of_enemies):
                enemy_image = pygame.image.load('enemy2.png')
                enemyImg.append(enemy_image)
                enemyX.append(random.randint(0, 735))
                enemyY.append(random.randint(50, 150))
                enemyX_change.append(0.6)

        if nivel_actual == 3:
            level_text = over_font.render("Nivel 3", True, (0, 255, 0))
            screen.blit(level_text, (300, 250))
            pygame.display.update()
            pygame.time.delay(2000)  #2 segundos antes de continuar

            #restablece los enemigos con nuevas imágenes y velocidades
            num_of_enemies = 10
            enemy_destroyed = [False] * num_of_enemies  # Reinicia el seguimiento de enemigos destruidos
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []

            for i in range(num_of_enemies):
                enemy_image = pygame.image.load('enemy3.png')
                enemyImg.append(enemy_image)
                enemyX.append(random.randint(0, 735))
                enemyY.append(random.randint(50, 150))
                enemyX_change.append(0.9)

        if nivel_actual == 4:
            level_text = over_font.render("Nivel 4", True, (0, 255, 0))
            screen.blit(level_text, (300, 250))
            pygame.display.update()
            pygame.time.delay(2000)  #2 segundos antes de continuar

            # restablece los enemigos con nuevas imágenes y velocidades
            num_of_enemies = 11
            enemy_destroyed = [False] * num_of_enemies  # Reinicia el seguimiento de enemigos destruidos
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []

            for i in range(num_of_enemies):
                enemy_image = pygame.image.load('enemy4.png')
                enemyImg.append(enemy_image)
                enemyX.append(random.randint(0, 735))
                enemyY.append(random.randint(50, 150))
                enemyX_change.append(1.2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            enemyY[i] = random.randint(50, 150)
            if playerLives >= 1:
                playerLives -= 1
                print("Vidas restantes:", playerLives)
            elif playerLives == 0:
                game_over_text()
                running = False
                break

        if not enemy_destroyed[i]:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = enemy_velocidades[nivel_actual -1]
                enemyY[i] += 40
            elif enemyX[i] >= 736:
                enemyX_change[i] = -enemy_velocidades[nivel_actual -1]
                enemyY[i] += 40

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += nivel_scores[nivel_actual - 1]
                enemy_destroyed[i] = True
                #enemyX[i] = random.randint(0, 736)
                #enemyY[i] = random.randint(50, 150)

            if playerLives == 3:
                muerte_3 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (510, 15))
                muerte_2 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (475, 15))
                muerte_1 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (440, 15))
            elif playerLives == 2:
                muerte_2 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (475, 15))
                muerte_1 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (440, 15))
            elif playerLives == 1:
                muerte_1 = screen.blit(pygame.transform.scale(playerImg, (25, 25)), (440, 15))

            enemy(enemyX[i], enemyY[i], i)
    #end


    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()