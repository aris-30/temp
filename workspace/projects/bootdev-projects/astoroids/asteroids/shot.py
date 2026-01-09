from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y,radius)
        self.velocity=velocity
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
