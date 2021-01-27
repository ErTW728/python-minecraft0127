# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:06:18 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time 
while True:    
    x,y,z = mc.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+50
    mc.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.5)