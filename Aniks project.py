import pygame

pygame.init()
display_width = 800
display_height = 400
gameDisplay = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("Racer")
black = (0, 0, 0)
white = (0, 255, 255)
car_width = 73

clock = pygame.time.Clock()
carImg = pygame.image.load("racecar.png")


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def game_loop():
    x = (display_width * .8)
    y = (display_height * .4)
    gameExit = False
    x_change = 0
    y_change = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        car(x, y)

        if x > display_width - car_width or x < 0:
            gameExit = True
        if y > display_height -car_width or y < 0:
            gameExit = True
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
