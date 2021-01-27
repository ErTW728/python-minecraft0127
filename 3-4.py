# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:46:59 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        mc.createExplosion(x,y,z,power=199)