#This is for notes on 9-11
#Python notes

#In terminal, you can start by creating a virtual environment, but I start in VScode so idk

#Create the python file itself
#This is specifically for a tic tac toe game
from matplotlib import pyplot as plt
import numpy as np
#Numpy library handles matricies and whatnot


class TTTBoard:
    def __init__(self):
        self.state = np.zeroes(shape=(3,3), dtype = int) #Creates an empty 3 by 3, two dimensional array of int data type filled with zeroes

    def check_win(self):
        self.state
        

class Game:
    def __init__(self):
        self.board = TTTBoard()

if __name__ == "__main__": #If this file is called as the main file, anything in this block will run
    game = Game()
    print(game.board.state) #Useful for debugging