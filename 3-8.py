# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:01:55 2021

@author: user
"""

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for a in range(10):
    for i in range(10):
        for u in range(10):
            plantTree(x+i*5,y+u*5,z+a*5)