

import random
import pygame

pygame.init()

# Устанавливаем размеры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Цвета для молекул
colors = [(220, 20, 60), (255, 69, 0), (255, 215, 0), (255, 0, 255), (30, 144, 255), (105, 105, 105), (240, 255, 240)]
class Molecule:
    def __init__(self):
        self.size = random.randint(5, 20)
        self.color = random.choice(colors)
        self.x = random.randint(1, 600)
        self.y = random.randint(1, 800)
        self.speed_x = random.randint(-20, 20)  # Замедлим скорость движения
        self.speed_y = random.randint(-20, 20)  # Замедлим скорость движения

    def move(self):
        self.x += self.speed_x  # Обновление позиции молекулы по оси x
        self.y += self.speed_y  # Обновление позиции молекулы по оси y
        clock = pygame.time.Clock()

        for other_molecule in molecules:
            if other_molecule != self:
                distance = ((self.x - other_molecule.x) ** 2 + (self.y - other_molecule.y) ** 2) ** 0.5
                min_dist = self.size + other_molecule.size # сумма радиусов сталкивающихся молекул.
                # минимум, который должен быть между молекулами, при достижении к-рого они меняют направление

                if distance < min_dist:
                    # Перемещаем молекулы, чтобы они не заходили друг на друга
                    dist = ((self.x - other_molecule.x) ** 2 + (self.y - other_molecule.y) ** 2) ** 0.5
                    overlap = (min_dist - dist) / 2
                    self.x += overlap * (self.x - other_molecule.x) / dist
                    self.y += overlap * (self.y - other_molecule.y) / dist
                    # Отталкивание молекул друг от друга
                    self.speed_x = -self.speed_x
                    self.speed_y = -self.speed_y

        # Отталкивание от краев экрана и изменение направления скорости
        if self.x <= self.size:  # Если молекула касается левой границы экрана
            self.speed_x = abs(self.speed_x)  # Изменяем направление скорости по x
        elif self.x >= width - self.size:  # Если молекула касается правой границы экрана
            self.speed_x = -abs(self.speed_x)  # Изменяем направление скорости по x

        if self.y <= self.size:  # Если молекула касается верхней границы экрана
            self.speed_y = abs(self.speed_y)  # Изменяем направление скорости по y
        elif self.y >= height - self.size:  # Если молекула касается нижней границы экрана
            self.speed_y = -abs(self.speed_y)  # Изменяем направление скорости по y
        clock.tick(800)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


molecules = [Molecule() for _ in range(20)]

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for molecule in molecules:
        molecule.move()
        molecule.draw()

    pygame.display.flip()

pygame.quit()