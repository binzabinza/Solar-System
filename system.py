#!/usr/bin/env python

'''
Python based simulation of the solar system.

For this simulation, the mass of the sun is considered so much greater than any of the planets, that each planet will be evaluated as a 2-body problem, ignoring the gravitational forces of any other planets.

A Runge-Kutta Method for solvind ODEs will be using to update position, velocity, and acceleration

All units are standard SI units. (meters, seconds, kilograms, etc)

John Binzer
'''

import sys
import math
import pygame
import time

#define colors for pygame windows
WHITE = (255, 255, 255)

#defines the window size for the simulation
WIDTH, HEIGHT = 900, 600

#defines big G
G = 6.67408*pow(10, -11)

#lets make 300 pixels = 1 au = 150000000000m
P2M = 2*pow(10, -9) #pixels/meter
class Planet:

    def __init__(self, m, x, y, vx, vy):
        #where m is the mass; (x, y) is the initial starting spatial coordinates; vx and vy are the intial starting velocities.
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def print_state(self):
        #prints the state of the planet: "Position: (x, y) Velocity: (vx, vy)"
        print "Position: (" + str(self.x) + ", " + str(self.y) + " Velocity: (" + str(self.vx) + ", " + str(self.vy) + ")"
        
    def update(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def main():
    #setting up the display window
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    #initializing the celestial bodies
    sun = Planet(1.989*pow(10, 30), 0, 0, 0, 0)
    earth = Planet(5.972*pow(10, 24), 150000000000, 0, 0, 30000)
    
    #integration time
    dt = 86400  #second

    #main loop of the program
    i = 0
    while (i < 365):
        r  = math.sqrt(pow(sun.x-earth.x, 2) + pow(sun.y-earth.y, 2))
        rx = sun.x-earth.x
        ry = sun.y-earth.y

        axsun = (G*earth.m)*(-rx)/pow(r, 3)
        aysun = (G*earth.m)*(-ry)/pow(r, 3)
        axearth = (G*sun.m)*(rx)/pow(r, 3)
        ayearth = (G*sun.m)*(ry)/pow(r, 3)

        vxsun = sun.vx + axsun*dt
        vysun = sun.vy + aysun*dt
        vxearth = earth.vx + axearth*dt
        vyearth = earth.vy + ayearth*dt

        xsun = sun.x + vxsun*dt
        ysun = sun.y + vysun*dt
        xearth = earth.x + vxearth*dt
        yearth = earth.y + vyearth*dt
        
        sun.update(xsun, ysun, vxsun, vysun)
        earth.update(xearth, yearth, vxearth, vyearth)

        #sun.print_state()
        pygame.draw.circle(window, WHITE, (int(sun.x*P2M) + WIDTH/2, int(sun.y*P2M) + HEIGHT/2), 40, 0) 
        #earth.print_state()
        pygame.draw.circle(window, WHITE, (int(earth.x*P2M + WIDTH/2), int(earth.y*P2M) + HEIGHT/2), 2, 0)
        pygame.display.update()
        time.sleep(0.01)

        i += 1
    
    time.sleep(10)

main()
