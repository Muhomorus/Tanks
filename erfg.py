import os
import pygame

from time import sleep


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 50
        self.top = 50
        self.cell_size = 10

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color('white'), (self.top + self.cell_size * i, self.left + self.cell_size * j,
                                                       self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x = (((self.width * self.cell_size) - (mouse_pos[0] - self.left)) // self.cell_size) - (self.width - 1)
        y = (((self.height * self.cell_size) - (mouse_pos[1] - self.top)) // self.cell_size) - (self.height - 1)
        if (-1 * self.width) < x < 1 and (-1 * self.height) < y < 1:
            return abs(x), abs(y)
        else:
            return None

    def on_click(self, cell_cords):
        print(cell_cords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)











class Tank:
    def __init__(self, speed, hp, bullet_type, tank, pos_x=0, pos_y=0):
        self.speed = speed
        self.hp = hp
        self.bullet_type = bullet_type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tank = tank

        self.move_count = 0

    def move(self):
        self.move_count += 1
        if self.move_count == self.speed:
            self.move_count = 0
            return True
        return False

    def new_cords(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def new_tank(self, tank):
        self.tank = tank













def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image
gh = load_image('tank.png')
print(type(gh))
gh = pygame.transform.rotate(gh, 180)
# gh = pygame.transform.rotate(gh, 90)
# gh = pygame.transform.rotate(gh, 90)
# self.enl = pygame.transform.rotate(self.enu, 90)
# self.enr = pygame.transform.rotate(self.enu, 270)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    #  board = Board(60, 60)
    running = True
    pos = [50, 50]
    fps = 10
    gov_no = 0
    dul = 0
    clock = pygame.time.Clock()
    while running:
        screen.fill(pygame.Color('purple'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    gov_no = event.key
                if event.key == pygame.K_a:
                    gov_no = event.key
                if event.key == pygame.K_s:
                    gov_no = event.key
                if event.key == pygame.K_d:
                    gov_no = event.key

            elif event.type == pygame.KEYUP:
                if event.key == gov_no:
                    gov_no = 0



        if gov_no == 100 and pos[0] + 10 <= 620:
            if dul != 1:
                if dul == 3:
                    gh = pygame.transform.rotate(gh, 90)
                    dul = 2
                    screen.blit(gh, pos)
                    #   board.render(screen)
                    pygame.display.flip()
                    sleep(0.3)
                if dul == 2:
                    gh = pygame.transform.rotate(gh, 90)
                    screen.blit(gh, pos)
                    #   board.render(screen)
                    pygame.display.flip()
                    dul = 1
                    sleep(0.3)
                if dul == 0:
                    gh = pygame.transform.rotate(gh, 270)
                    screen.blit(gh, pos)
                    #  board.render(screen)
                    pygame.display.flip()
                    dul = 1
                    sleep(0.3)
            pos[0] += 10


        if gov_no == 115 and pos[1] + 10 <= 620:
            if dul != 2:
                if dul == 0:
                    gh = pygame.transform.rotate(gh, 90)
                    dul = 3
                    screen.blit(gh, pos)
                    #  board.render(screen)
                    pygame.display.flip()
                    sleep(0.3)
                if dul == 3:
                    gh = pygame.transform.rotate(gh, 90)
                    screen.blit(gh, pos)
                    #   board.render(screen)
                    pygame.display.flip()
                    dul = 2
                    sleep(0.3)
                if dul == 1:
                    gh = pygame.transform.rotate(gh, 270)
                    screen.blit(gh, pos)
                    #    board.render(screen)
                    pygame.display.flip()
                    dul = 2
                    sleep(0.3)
            pos[1] += 10


        if gov_no == 97 and pos[0] - 10 >= 50:
            if dul != 3:
                if dul == 1:
                    gh = pygame.transform.rotate(gh, 90)
                    dul = 0
                    screen.blit(gh, pos)
                    #    board.render(screen)
                    pygame.display.flip()
                    sleep(0.3)
                if dul == 0:
                    gh = pygame.transform.rotate(gh, 90)
                    screen.blit(gh, pos)
                    #  board.render(screen)
                    pygame.display.flip()
                    dul = 3
                    sleep(0.3)
                if dul == 2:
                    gh = pygame.transform.rotate(gh, 270)
                    screen.blit(gh, pos)
                    #  board.render(screen)
                    pygame.display.flip()
                    dul = 3
                    sleep(0.3)
            pos[0] -= 10


        if gov_no == 119 and pos[1] - 10 >= 50:
            if dul != 0:
                if dul == 2:
                    gh = pygame.transform.rotate(gh, 90)
                    dul = 1
                    screen.blit(gh, pos)
                    #   board.render(screen)
                    pygame.display.flip()
                    sleep(0.3)
                if dul == 1:
                    gh = pygame.transform.rotate(gh, 90)
                    screen.blit(gh, pos)
                    #   board.render(screen)
                    pygame.display.flip()
                    dul = 0
                    sleep(0.3)
                if dul == 3:
                    gh = pygame.transform.rotate(gh, 270)
                    screen.blit(gh, pos)
#                    board.render(screen)
                    pygame.display.flip()
                    dul = 0
                    sleep(0.3)
            pos[1] -= 10


        print(type(gh))
        screen.blit(gh, pos)
        #         board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
        pygame.mouse.set_visible(False)

        pygame.display.flip()