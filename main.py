#   File: main.py
# Unnecessary comment

from pygame import *;
from game import *;
from menu import *;
from highs import *
import os;

STATE_MENU = 1
STATE_GAME = 2
STATE_DEMO = 3
STATE_HIGH = 4
STATE_KILL = 5

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        #Init the modules we need
        display.init()
        pygame.mixer.init()
        font.init()
        
        if(Config.GAME_FULLSCREEN == True):
            self.screen = display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = display.set_mode((1024, 768))
            
        display.set_caption('ATC Version 0.1')

        self.menu = Menu(self.screen)
        self.high = HighScore(self.screen)
        # Number of airplanes
        self.n_airplanes = int(input('Number of Airplanes : '))

    def run(self):
        state = STATE_MENU ####
        exit = 0
        score = 0

        while (exit == 0):
             if (state == STATE_MENU):
                 menuEndCode = None
                 menuEndCode = self.menu.start()
                 if (menuEndCode == Config.MENU_CODE_START):
                     state = STATE_GAME
                 elif (menuEndCode == Config.MENU_CODE_DEMO):
                     state = STATE_DEMO
                 elif (menuEndCode == Config.MENU_CODE_HIGH_SCORE):
                     state = STATE_HIGH
                 elif (menuEndCode == Config.CODE_KILL):
                     state = STATE_KILL
             elif (state == STATE_GAME):
                 game = Game(self.screen, False)
                 (gameEndCode, score) = game.start(n_airplanes = self.n_airplanes)
                 if (gameEndCode == Config.GAME_CODE_TIME_UP):
                     state = STATE_GAME ###
                 elif (gameEndCode == Config.CODE_KILL):
                     state = STATE_GAME ###
                 elif (gameEndCode == Config.GAME_CODE_USER_END):
                     state = STATE_MENU
                 elif (gameEndCode == Config.GAME_CODE_AC_COLLIDE):
                     state = STATE_GAME ###
             elif (state == STATE_DEMO):
                game = Game(self.screen, True)
                (gameEndCode, score) = game.start()
                state = STATE_MENU
             elif (state == STATE_HIGH):
                 highEndCode = self.high.start(score)
                 state = STATE_GAME     #####
                 score = 0
             elif (state == STATE_KILL):
                 exit = 1

if __name__ == '__main__':
    game_main = Main()
    game_main.run()