import pygame

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

START_BUTTON = pygame.image.load('START.PNG').convert_alpha()
STOP_BUTTON = pygame.image.load('STOP.PNG').convert_alpha()
TRIP_REPORT_BUTTON = pygame.image.load('Trip_Report.PNG').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        position = pygame.mouse.get_pos()
        print(position)

        screen.blit(self.image, (self.rect.x, self.rect.y))


start_button = Button(297.5, 50, START_BUTTON, 1.0)
stop_button = Button(216.5, 200, STOP_BUTTON, 1.0)
trip_report_button = Button(300, 350, TRIP_REPORT_BUTTON, 1.0)

run = True
while run:
    screen.fill((229, 229, 229))

    start_button.draw()
    stop_button.draw()
    trip_report_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()    

