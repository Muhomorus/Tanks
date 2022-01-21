import pygame
import os


pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)

run_for_t1 = False
run_for_t2 = False
run_for_red = False

def start():
    global run_for_t1, run_for_t2, run_for_red, q

    pygame.init()
    pygame.display.set_caption('q1')
    running_for_main_window = True
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont(None, 150)
    screen.fill((200, 255, 200))
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(10, 10, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 160, 520, 120), 2)
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(170, 440, 520, 120), 2)
    screen.blit(font.render('Редактор', True, "pink"), (18, 20))
    screen.blit(font.render('Уровни', True, "pink"), (184, 170))
    screen.blit(font.render('PVP', True, "pink"), (330, 450))
    pygame.display.flip()
    while running_for_main_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_for_main_window = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(10, 10, 520, 120).collidepoint(event.pos):
                    run_for_red = True
                    check()
                elif pygame.Rect(170, 160, 520, 120).collidepoint(event.pos):
                    run_for_t1 = True
                    check()
                if pygame.Rect(170, 440, 520, 120).collidepoint(event.pos):
                    run_for_t2 = True
                    check()



def check():
    global run_for_t2, run_for_t1, run_for_red
    if run_for_t1:
        os.system('python main.py')
        run_for_t1 = False
    elif run_for_t2:
        os.system('python 1plaer.py')
        run_for_t2 = False
    elif run_for_red:
        os.system('python dffghf.py')
        run_for_red = False
    start()

start()
