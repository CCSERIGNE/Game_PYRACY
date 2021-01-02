import pygame

from game import Game, CYAN, GREY, RED, BLUE
from car import Car
from speedway import Speedway

class PyRace(Game):
    carWidth = 100
    carHeight = 150
    moveSpeed = 5

    def buildItems(self):
        
        speedway = Speedway(self.width, self.height)
        self.allSprites.add(speedway)
        positionX1 = (self.width/2.4) - self.carWidth
        positionX2 = self.width/1.7

        player = Car(CYAN, self.carWidth, self.carHeight, True)
        player.rect.x = positionX1
        player.rect.y = (self.height/1.02) - self.carHeight
        self.allSprites.add(player)
        self.player = player

        self.opponents = pygame.sprite.Group()

        opponentRed = Car(RED, self.carWidth, self.carHeight, False)
        opponentRed.rect.x = positionX1
        opponentRed.rect.y = -50
        self.allSprites.add(opponentRed)
        self.opponents.add(opponentRed)

        opponentBlue = Car(BLUE, self.carWidth, self.carHeight, False)
        opponentBlue.rect.x = positionX2
        opponentBlue.rect.y = -500
        self.allSprites.add(opponentBlue)
        self.opponents.add(opponentBlue)

    def handleEvent(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.moveLeft(self.moveSpeed)
        if keys[pygame.K_RIGHT]:
            self.player.moveRight(self.moveSpeed)

        if pygame.sprite.spritecollide(self.player, self.opponents, False):
            self.player.crash()
        
        for opponent in self.opponents:
            if not opponent.rect.colliderect(self.display.get_rect()) and opponent.rect.y > 0:
                opponent.rect.y = -200

PyRace('PyRace', 400, 650)