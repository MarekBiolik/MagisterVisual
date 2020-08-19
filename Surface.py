import pygame
import Colors as c
from Segment import Segment
from Segment import SegmentType

########################################################################
# Global settings:
SIZE = 1000           # size of display window for single instance
STATUS_HEIGHT = 10   # height of status bar in display window
STATUS_HEIGHT2 = 10  # height of status bar within instance subwindows
DELIM_WIDTH = 5      # width of delimiter between direct and sim. ann. output
CITY_RADIUS = 7      # radius of circle representing city
SLEEP = 400          # delay (in seconds) after plotting new configuration

class Surface:

    def __init__(self):
        pygame.init()
        self.helv24 = pygame.font.SysFont("Helvetica", 24)
        self.SWIDTH = SIZE + DELIM_WIDTH + DELIM_WIDTH
        self.SHEIGHT = SIZE + STATUS_HEIGHT + STATUS_HEIGHT2
        self.surface = pygame.display.set_mode((self.SWIDTH, self.SHEIGHT))
        self.surface.set_alpha(None)

    def draw_text(self, text, position, color):
        # draw user-defined text in pygame graphics surface
        lable = self.helv24.render(text, 1, color)
        self.surface.blit(lable, position)

    def create(self, diters, countOfVertexs, distances):
        self.surface.fill(c.COLORS["WHITE"])
        self.surface.fill(c.COLORS["LIGHTYELLOW"], (0, 0, 2 * SIZE + DELIM_WIDTH, STATUS_HEIGHT))
        self.surface.fill(c.COLORS["DARKBLUE"], (0, STATUS_HEIGHT, DELIM_WIDTH, SIZE + STATUS_HEIGHT2))
        self.surface.fill(c.COLORS["DARKBLUE"], (SIZE + DELIM_WIDTH, STATUS_HEIGHT, DELIM_WIDTH, SIZE + STATUS_HEIGHT2))
        self.surface.fill(c.COLORS["DARKBLUE"], (0, SIZE + STATUS_HEIGHT + STATUS_HEIGHT2 - DELIM_WIDTH, 2 * SIZE + DELIM_WIDTH, DELIM_WIDTH)) # dol
        self.surface.fill(c.COLORS["DARKBLUE"], (0, STATUS_HEIGHT, 2 * SIZE + DELIM_WIDTH, DELIM_WIDTH)) # gora
        self.draw_text("No of cities:", (110, 15), c.COLORS["BLACK"])
        self.draw_text(str(countOfVertexs), (250, 15), c.COLORS["BLUE"])
        self.draw_text("Iterations:", (30, STATUS_HEIGHT + 30), c.COLORS["BLACK"])
        self.draw_text(str(diters), (150, STATUS_HEIGHT + 32), c.COLORS["BLUE"])
        self.draw_text("Tour Length:", (260, STATUS_HEIGHT + 30), c.COLORS["BLACK"])
        self.draw_text(str(distances[diters]), (410, STATUS_HEIGHT + 32), c.COLORS["BLUE"])

    def drawCity(self, x, y, radiusNeighbour):
        pygame.draw.circle(self.surface, c.COLORS["PINK"], [int(x) + 100, int(y) + 100], CITY_RADIUS)
        pygame.draw.circle(self.surface, c.COLORS["GREEN"], [int(x) + 100, int(y) + 100], radiusNeighbour, 2)

    def updateGraphicsOutput(self):
        pygame.display.flip()

    def drawArc(self, segment, r):
        point, fstPoint, sndPoint = segment.calculateArc(r)
        xb = segment.sndPoint.x
        yb = segment.sndPoint.y
        pygame.draw.circle(self.surface, c.COLORS["BLUE"], [int(xb) + 100, int(yb) + 100], 4)
        pygame.draw.arc(self.surface, c.COLORS["BLUE"], point, fstPoint, sndPoint, 3)

    def drawStraigh(self, segment):
        fstPoint = segment.fstPoint
        sndPoint = segment.sndPoint
        xa = fstPoint.x
        ya = fstPoint.y
        xb = sndPoint.x
        yb = sndPoint.y
        pygame.draw.circle(self.surface, c.COLORS["BLUE"], [int(xb + 100), int(yb + 100)], 4)
        pygame.draw.line(self.surface, c.COLORS["DARKGREY"],
                         [xa + 100, ya + 100], [xb + 100, yb + 100], 3)

    def drawStartPoint(self, segment):
        fstPoint = segment.fstPoint
        xa = fstPoint.x
        ya = fstPoint.y
        pygame.draw.circle(self.surface, c.COLORS["BROWN"], [int(xa + 100), int(ya + 100)], 8)

    def drawSegment(self, segment, r, drawStartPoint):
        if (drawStartPoint):
            self.drawStartPoint(segment)
        if (segment.typeOfSegment == SegmentType.Stra):
            self.drawStraigh(segment)
        else:
            # x, y = segment.findMiddleOfCircle(r)
            # pygame.draw.circle(surface, c.COLORS["PINK"], [int(x), int(y)], CITY_RADIUS)
            self.drawArc(segment, r)