import pygame
from EventManager import EventHandler

class Window:
    def __init__ (self, resx, resy):

        pygame.init()

        self.width = resx
        self.height = resy
        self.master_surface = pygame.display.set_mode((self.width, self.height))

        self.event_handler = EventHandler()
        self.event_handler.state = "Running"


    def start_mainloop (self):
        while True:
            self.event_handler.cycle()

            pygame.display.flip()



