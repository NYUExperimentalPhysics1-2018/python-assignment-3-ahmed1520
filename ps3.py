# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt




display_width = 800
display_height = 600


tank1Color = 'b'
tank2Color = 'r'
obstacleColor = 'k'



def trajectory (x0,y0,v,theta,g = 9.8, npts = 1000):
    x0: float
    y0: float
    theta: float
    g: float
    npts: int
    
    def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
        prompt: str
        validRange: list
        while True:
            try:
                num = float(input(prompt))
            except Exception:
                print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") 
            
    return num 


def drawBoard(tank1box, tank2box, obstacleBox, playerNum):
     tank1box: tuple
tuple(10,15,0,5)
tank2box: tuple
tuple(90,95,0,5)
obstacleBox: tuple
tuple(40,60,0,5)
playerNum: 1
    
def playGame(tank1box, tank2box, obstacleBox, g = 9.8):
    tank1box: tuple
    tuple(10,15,0,5)
    tank2box: tuple
    tuple(90,95,0,5)
    obstacleBox: tuple
    tuple(40,60,0,5)
    playerNum: 1
    g: float
    
    def showWindow():
        plt.draw()
    plt.pause(0.001)
    plt.show()
    
    def drawBox(box, color):
        box: tuple
        tuple(0,100,0,50)
        color:str
    x = (box[0], box[0], box[1], box[1])
    y = (box[2], box[3], box[3], box[2])
    ax = plt.gca()
    ax.fill(x,y, c = color)

def endTrajectoryAtIntersection (x,y,box):
    x,y : np.array
    box : tuple
    tuple(0,100,0,50)        
    i = firstInBox(x,y,box)
    if (i < 0):
        return (x,y)
    return (x[0:i],y[0:i])
def main():
    tank1box = [10,15,0,5]
    tank2box = [90,95,0,5]
    obstacleBox = [40,60,0,50]
    playGame(tank1box, tank2box, obstacleBox)
    