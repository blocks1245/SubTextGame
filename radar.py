import pygame
import math

EntityTypeError = False
done = False
FPSCLOCK = pygame.time.Clock()

SizeScreen = (1000, 800)
screen = pygame.display.set_mode(SizeScreen)
RadarPos = (500, 250)
RadarSize = 200
AngleLine = 0
SpeedLine = 1

Red = (255, 000, 000)
Green = (000, 255, 000)
Blue = (000, 000, 255)

PlayerPos = (0, 0, 0)  # x, Y, rotation(0-360)
EntityID = 0
EntityList = (
    77, 50, 'Enemy',
    -10, -50, 'Enemy',
    10, 10, 'Fuel',
    -80, 80, 'Fel',
    100, 80, 'Enemy',
    -50, -60, 'Fuel'
)


class Radar:
    def __init__(self, x, y, Type, RadarPrecision):
        self.x = x * RadarPrecision
        self.y = y * RadarPrecision
        self.Type = Type
        self.distance = math.sqrt(x * x + y * y)

        # Rotating line
        self.startpoint = pygame.math.Vector2(RadarPos)
        self.endpoint = pygame.math.Vector2(RadarSize, 0)
        self.current_endpoint = self.startpoint + self.endpoint.rotate(AngleLine)

        # Background
        pygame.draw.circle(screen, Green, RadarPos, 3, 3)
        pygame.draw.circle(screen, Green, RadarPos, RadarSize, 1)
        pygame.draw.circle(screen, Green, RadarPos, int(RadarSize / 2), 1)
        pygame.draw.line(screen, Green, (RadarPos[0], RadarPos[1] + RadarSize), (RadarPos[0], RadarPos[1] - RadarSize), 1)
        pygame.draw.line(screen, Green, (RadarPos[0] + RadarSize, RadarPos[1]), (RadarPos[0] - RadarSize, RadarPos[1]), 1)

        # Entity class
        if self.distance <= RadarSize / 2:
            if self.Type == 'Enemy':
                pygame.draw.circle(screen, Red, (int(self.x + RadarPos[0]), int(-self.y + RadarPos[1])), 4, 1)
            elif self.Type == 'Fuel':
                pygame.draw.circle(screen, Green, (int(self.x + RadarPos[0]), int(-self.y + RadarPos[1])), 4, 1)

        # rotating line
        pygame.draw.line(screen, Green, self.startpoint, self.current_endpoint, 2)


while not done:

    screen.fill((0, 0, 0))
    # drawing Entity's
    for i in range(int(len(EntityList) / 3)):
        EntityID = i * 3
        EntityX = EntityList[EntityID]
        EntityY = EntityList[EntityID + 1]
        EntityType = EntityList[EntityID + 2]
        Radar(EntityX, EntityY, EntityType, RadarSize / 100)
        i = + 1

    AngleLine = (AngleLine + SpeedLine) % 360
    pygame.display.flip()
    FPSCLOCK.tick(30)

    # X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True