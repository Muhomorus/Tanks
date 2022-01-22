import pygame
import os


pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
lev_dict = {}


def levelis(q):
    if q == 0:
        return lev_dict[0]
    if q == 1:
        return lev_dict[1]
    if q == 2:
        return lev_dict[2]
    if q == 3:
        return lev_dict[3]



def start():
    pygame.init()
    pygame.display.set_caption('q1')
    size = width, height = 700, 570
    screen = pygame.display.set_mode(size)


    font = pygame.font.SysFont(None, 145)
    screen.fill("purple")
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(10, 10, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 160, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(10, 300, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 440, 520, 120), 2)
    screen.blit(font.render('Уровень 1', True, "pink"), (17, 20))
    screen.blit(font.render('Уровень 2', True, "pink"), (184, 170))
    screen.blit(font.render('Уровень 3', True, "pink"), (17, 310))
    screen.blit(font.render('Уровень 4', True, "pink"), (184, 450))

    pygame.display.flip()
    running_for_levels = True
    while running_for_levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_for_levels = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(10, 10, 520, 120).collidepoint(event.pos):
                    levelis(0)
                if pygame.Rect(170, 160, 520, 120).collidepoint(event.pos):
                    levelis(1)
                if pygame.Rect(10, 300, 520, 120).collidepoint(event.pos):
                    levelis(2)
                if pygame.Rect(170, 440, 520, 120).collidepoint(event.pos):
                    levelis(3)



if __name__ == '__main__':
    start()
pygame.quit()


