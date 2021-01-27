# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:35:19 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(0,20):
    mc.setBlock(x+i,y-1,z+i,41)
    mc.setBlock(x+i+1,y-1,z+i,41)
    mc.setBlock(x+i+2,y-1,z+i,41)
    mc.setBlock(x+i+3,y-1,z+i,41)