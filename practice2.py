# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:01:51 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        mc.spawnEntity(x,y,z,99)
        mc.player.setTilePos(x,y,z)