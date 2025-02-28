from src.settings import *

class NewProject:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.frame = pg.Surface((self.win.width // 1.2,self.win.height // 1.2))

        self.active = True

    def render(self):
        if self.active:
            self.win.blit(self.frame,(self.win.width // 2 - self.frame.width // 2,
                                      self.win.height // 2 - self.frame.height // 2))

    def update(self):
        if self.active:
            pass