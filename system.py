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
    
    planets = [earth]
    #integration time
    dt = 86400  #seconds

    #main loop of the program
    i = 0
    while (i < 3650):
        for planet in planets:
            r  = math.sqrt(pow(sun.x-planet.x, 2) + pow(sun.y-planet.y, 2))
            rx = sun.x-planet.x
            ry = sun.y-planet.y

            axsun = (G*planet.m)*(-rx)/pow(r, 3)
            aysun = (G*planet.m)*(-ry)/pow(r, 3)
            axplanet = (G*sun.m)*(rx)/pow(r, 3)
            ayplanet = (G*sun.m)*(ry)/pow(r, 3)

            vxsun = sun.vx + axsun*dt
            vysun = sun.vy + aysun*dt
            vxplanet = planet.vx + axplanet*dt
            vyplanet = planet.vy + ayplanet*dt

            xsun = sun.x + vxsun*dt
            ysun = sun.y + vysun*dt
            xplanet = planet.x + vxplanet*dt
            yplanet = planet.y + vyplanet*dt
        
            sun.update(xsun, ysun, vxsun, vysun)
            planet.update(xplanet, yplanet, vxplanet, vyplanet)

            pygame.draw.circle(window, WHITE, (int(sun.x*P2M) + WIDTH/2, int(sun.y*P2M) + HEIGHT/2), 40, 0) 
            pygame.draw.circle(window, WHITE, (int(planet.x*P2M + WIDTH/2), int(planet.y*P2M) + HEIGHT/2), 2, 0)
        
        pygame.display.update()
        time.sleep(0.01)
        i += 1
    
    time.sleep(10)

main()
