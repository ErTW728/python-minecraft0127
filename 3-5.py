# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:23:44 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(0,20):
    mc.setBlock(x,y-1,z+i,41)