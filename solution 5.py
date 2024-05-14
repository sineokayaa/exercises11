import random
import pygame

pygame.init()


class Molecule:
    '''
    A class representing a molecule.
    '''
    screen = pygame.display.set_mode((800, 700))
    colors = [(220, 20, 60), (255, 69, 0), (255, 215, 0), (255, 0, 255), (30, 144, 255),
              (105, 105, 105), (240, 255, 240)]
    width = 800
    height = 700
    all_molecules = []

    def __init__(self):
        self.color = random.choice(Molecule.colors)
        self.radius = random.randint(5, 19)
        self.x = random.randint(20, Molecule.height-20)
        self.y = random.randint(20, Molecule.width-20)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        Molecule.all_molecules.append(self)

    def __str__(self):
        return f'{self.color}-{self.radius}'

    def __repr__(self):
        return str(f'{self.color}-{self.radius}')

    def moving_molecule(self):
        '''
        Move the molecule within the screen boundaries.
        '''

        clock = pygame.time.Clock()

        if self.x + self.radius + self.speed_x >= Molecule.width:
            self.speed_x = -self.speed_x
        if self.y + self.radius + self.speed_y >= Molecule.height:
            self.speed_y = -self.speed_y
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= self.radius:
            self.speed_x = -self.speed_x
        elif self.x >= Molecule.width - self.radius:
            self.speed_x = -self.speed_x

        if self.y <= self.radius:
            self.speed_y = -self.speed_y
        elif self.y >= Molecule.height - self.radius:
            self.speed_y = -self.speed_y

        for oth_molecule in Molecule.all_molecules:
            if oth_molecule != self:
                dist = ((self.x - oth_molecule.x) ** 2 + (self.y - oth_molecule.y) ** 2) ** 0.5
                if dist < self.radius + oth_molecule.radius:
                    self.speed_x = - self.speed_x
                    self.speed_y = - self.speed_y
                    oth_molecule.speed_x = - oth_molecule.speed_x
                    oth_molecule.speed_y = - oth_molecule.speed_y

        clock.tick(1000)

    def draw(self):
        '''
        Draw the molecule within the screen boundaries.
        '''
        pygame.draw.circle(Molecule.screen, self.color, (self.x, self.y), self.radius)


for _ in range(20):
    Molecule()
print(Molecule.all_molecules)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Molecule.screen.fill((0, 0, 0))

    for molecule in Molecule.all_molecules:
        Molecule.draw(molecule)
        Molecule.moving_molecule(molecule)

    pygame.display.flip()

pygame.quit()
