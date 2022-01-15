import pyglet as pg
from random import random, randint
from cards import Card, cardHeight, cardWidth
xRadius = 0.0
yRadius = 0.0
usedDeck = None
deck = None
class Player:
    won = False
    playerCount = 4
    turn = 0
    def __init__(self, position, playable, window):
        self.position = position
        self.playable = playable
        self.window = window
        self.cards = []
        self.button_pressed = False
        self.selectedIndex = 0
        self.requestedToTakeCards = 0
        if(self.playable == False):
            self.waited = 0
        if(position == 0 or position == 2):
            self.maxSize = xRadius - 168.0
        elif(position == 1 or position == 3):
            self.maxSize = yRadius - 107.0
        self.addCards(7)
    def AI(self):
        if(self.waited < 20):
            self.waited += 1
            return
        self.waited = 0
        if(self.requestedToTakeCards != 0):
            for x in range(len(self.cards)):
                if self.cards[x].name == 'stop':
                    self.throwCard(x)
                    self.end_turn()
                    return
            self.addCards(self.requestedToTakeCards)
            self.end_turn()
            return
        playableIndexes = []
        lastCard = usedDeck.lastCard()
        for x in range(len(self.cards)):
            if(self.matchingCard(lastCard, self.cards[x])):
                playableIndexes.append(x)
        print(len(playableIndexes), self.position)
        if(len(playableIndexes) == 0):
            self.addCards(1)
            self.end_turn()
            return
        index = playableIndexes[randint(0, len(playableIndexes)-1)]
        self.throwCard(index)
        self.end_turn()
    def update(self, dt, keys):
        if(self.position == Player.turn):
            if(self.playable):
                self.select(dt, keys)
            else:
                self.AI()
        for card in self.cards:
            if(card.moving):
                card.move()
    def select(self, dt, keys):
        if(self.button_pressed == False):
            if(keys[pg.window.key.A]):
                if(self.selectedIndex > 0):
                    self.cards[self.selectedIndex].selected = False
                    self.selectedIndex -= 1
                    self.cards[self.selectedIndex].selected = True
                    self.button_pressed = True
            elif(keys[pg.window.key.D]):
                if(self.selectedIndex < len(self.cards) - 1):
                    self.cards[self.selectedIndex].selected = False
                    self.selectedIndex += 1
                    self.cards[self.selectedIndex].selected = True
                    self.button_pressed = True
            elif(keys[pg.window.key.ENTER]):
                self.button_pressed = True
                if(self.throwCard(self.selectedIndex) == False):
                    return
                if (Player.won == False):
                    self.selectedIndex = 0
                    self.cards[self.selectedIndex].selected = True
                    self.end_turn()
            elif(keys[pg.window.key.SPACE]):
                self.addCards(1)
                self.button_pressed = True
                self.end_turn()
        else:
            if(keys[pg.window.key.A] == False and keys[pg.window.key.D] == False and keys[pg.window.key.ENTER] == False and keys[pg.window.key.SPACE] == False):
                self.button_pressed = False
    def addCards(self, count):
        if(self.playable):
            for card in self.cards:
                card.selected = False
        self.selectedIndex = 0
        for x in range(count):
            card = Card()
            if(self.position == 0):
                card.zRot = 0.0
            elif(self.position == 1):
                card.zRot = 90.0
            elif(self.position == 2):
                card.zRot = 180.0
            elif(self.position == 3):
                card.zRot = 270.0
            if(self.playable):
                card.yRot = 180.0
            self.cards.append(card)
        self.positionCards()
        if(self.playable):
            self.cards[self.selectedIndex].selected = True
    def matchingCard(self, lastCard, card):
        if(lastCard.color == card.color or lastCard.color == None or card.color == None or lastCard.name == card.name):
            return True
        else:
            return False
    def throwCard(self, index):
        card = self.cards[index]
        if(self.matchingCard(usedDeck.lastCard(), card)):
            if(self.playable):
                card.selected = False
            usedDeck.add_card(card)
            self.cards.remove(card)
            if(len(self.cards) == 0):
                Player.won = True
                print("Player", self.position, "won")
            self.positionCards()
            return True
        return False
    def positionCards(self):
        if (len(self.cards)%2 == 0):
            parzyste = cardWidth/2+5
        else:
            parzyste = 0.0
        if(self.position % 2 == 0):
            horizontal = True
        else:
            horizontal = False
        lewo = 1
        counter = 0
        for card in self.cards:
            if(horizontal):
                card.x = lewo * (parzyste + counter * (cardWidth + 10) )
            else:
                card.y = lewo * (parzyste + counter * (cardWidth + 10) )
            if (lewo == 1 and parzyste == 0.0):
                counter += 1
            elif (lewo != 1 and parzyste != 0.0):
                counter += 1
            lewo *= -1

        def sorting(e):
            if(horizontal):
                return e.x
            else:
                return e.y
        self.cards.sort(key=sorting)
        for x in range(len(self.cards)):
            self.cards[x].setOrder(x)
            if(horizontal):
                if (self.cards[len(self.cards)-1].x > self.maxSize):
                    self.cards[x].x *= self.maxSize/self.cards[len(self.cards)-1].x
            else:
                if (self.cards[len(self.cards)-1].y > self.maxSize):
                    self.cards[x].y *= self.maxSize/self.cards[len(self.cards)-1].y
            if(self.position == 0):
                self.cards[x].y = -yRadius + cardHeight/2 + 20
            elif(self.position == 2):
                self.cards[x].y = (-yRadius + cardHeight/2 + 20) * -1
            elif(self.position == 1):
                self.cards[x].x = -xRadius + cardHeight/2 + 20
            elif(self.position == 3):
                self.cards[x].x = (-xRadius + cardHeight/2 + 20) * -1
            self.cards[x].moving = True
    def end_turn(self):
        Player.turn = (Player.turn + 1) % Player.playerCount
    def draw(self):
        pg.graphics.glPushMatrix()
        for card in self.cards:
            card.draw()
        pg.graphics.glPopMatrix()
class Deck:
    def __init__(self, depth):
        self.depth = depth
        self.card = Card("stop", None, -40.0)
        self.card.distance = depth
    def draw(self):
        self.card.draw()
class Used:
    def __init__(self):
        firstCard = Card()
        firstCard.x = 0
        firstCard.y = 0
        firstCard.yRot = 180.0
        firstCard.moving = True
        self.cards = [firstCard]
        self.xloc = 0.0
        self.yloc = 0.0
        self.zRot = 0.0
        self.counter = 0
    def add_card(self, card):
        if(len(self.cards) >= 10):
            self.cards.pop(0)
        card.x = self.xloc
        card.y = self.yloc
        card.zRot = (self.zRot + random() * 100.0 - 50.0) % 360.0
        card.yRot = 180.0
        card.moving = True
        card.setOrder(self.counter)
        self.counter += 1
        self.cards.append(card)
    def lastCard(self):
        return self.cards[len(self.cards)-1]
    def draw(self):
        pg.graphics.glPushMatrix()
        for card in self.cards:
            card.draw()
        pg.graphics.glPopMatrix()
    def update(self, dt):
        for card in self.cards:
            if(card.moving):
                card.move()