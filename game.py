import pygame

BLACK = (0, 0, 0)
GREEN = (84, 171, 71)
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

class Game:
    def __init__(self, title='Game', width=800, height=600, tick=30):
        self.width = width
        self.height = height
        self.tick = tick
        self.allSprites = pygame.sprite.Group()
        
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.loop()
    
    def __del__(self):
        pygame.quit()
    
    def handleEvent(self, event):
        pass

    def buildItems(self):
        pass

    def updateItems(self):
        pass

    def loop(self):
        clock = pygame.time.Clock()
        self.buildItems()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handleEvent(event)
            self.handleEvent(None)

            self.display.fill((GREY))
            self.updateItems()
            self.allSprites.update()
            self.allSprites.draw(self.display)

            pygame.display.update() 
            clock.tick(self.tick)
