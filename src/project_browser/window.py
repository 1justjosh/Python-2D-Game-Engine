from src.settings import *
from src.project_browser.new_project import NewProject

class Window:
    def __init__(self):
        self.win = pg.display.set_mode((720,520))
        pg.display.set_caption("Pygame 2D Project Browser")

        self.new_project = NewProject()

        self.clock = pg.time.Clock()
        self.running = True

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def render(self):
        self.win.fill((10,40,80))
        self.new_project.render()
        pg.display.flip()

    def update(self):
        self.clock.tick(60)
        self.new_project.update()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()

        pg.quit()
        sys.exit()