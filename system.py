#!/usr/bin/env python

'''
Python based simulation of the solar system.

For this simulation, the mass of the sun is considered so much greater than any of the planets, that each planet will be evaluated as a 2-body problem, ignoring the gravitational forces of any other planets.

All units are standard SI units. (meters, seconds, kilograms, etc)

John Binzer
'''

import sys
import math
import pygame
import time

#define colors for pygame windows
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
PALEYELLOW = (255, 255,153)
YELLOW     = (255, 255, 0)
RED        = (204, 0, 0)
ORANGE     = (255, 153, 51)
PALEBLUE   = (51, 153, 255)
BLUE       = (0, 51, 204)
GREEN      = (51, 204, 51)
BROWN      = (153, 102, 0)
PURPLE     = (153, 51, 153)

#defines the window size for the simulation
WIDTH, HEIGHT = 1920, 1200

#defines big G
G = 6.67408*pow(10, -11)

#lets make 300 pixels = 1 au = 150000000000m
P2M = 1.2334575*pow(10, -9) #pixels/meter
#P2M = 1.623541*pow(10,-10) 

class Planet:

    def __init__(self, m, x, y, vx, vy, color):
        #where m is the mass; (x, y) is the initial starting spatial coordinates; vx and vy are the intial starting velocities.
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def print_state(self):
        #prints the state of the planet: "Position: (x, y) Velocity: (vx, vy)"
        print "Position: (" + str(self.x) + ", " + str(self.y) + " Velocity: (" + str(self.vx) + ", " + str(self.vy) + ")"
        
    def update(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def timestamp(time, tfont, window):
    pygame.draw.rect(window, BLACK, (0, 0, 200, 35), 0)
    textSurface = tfont.render(time, True, WHITE)
    TextRect = textSurface.get_rect()
    TextRect.topleft = (0, 0)
    window.blit(textSurface, TextRect)
    pygame.display.update()

def make_objects():
    mercury = Planet(0.3311*pow(10, 24), 5.790*pow(10, 10), 0, 0, 47400, WHITE)
    venus   = Planet(4.8675*pow(10, 24), 1.082*pow(10, 11), 0, 0, 35025, GREEN)
    earth   = Planet(5.9723*pow(10, 24), 1.496*pow(10, 11), 0, 0, 29790, BLUE)
    mars    = Planet(6.4171*pow(10, 23), 2.279*pow(10, 11), 0, 0, 24070, RED)
    jupiter = Planet(1.8982*pow(10, 27), 7.783*pow(10, 11), 0, 0, 13060, ORANGE)
    saturn  = Planet(5.6834*pow(10, 26), 1.427*pow(10, 12), 0, 0, 9680, PALEYELLOW)
    uranus  = Planet(96.813*pow(10, 24), 2.871*pow(10, 12), 0, 0, 6800, PALEBLUE)
    neptune = Planet(1.0241*pow(10, 26), 4.497*pow(10, 12), 0, 0, 5430, PURPLE)
    pluto   = Planet(0.1303*pow(10, 23), 5.913*pow(10, 12), 0, 0, 4670, BROWN)
    return  [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]


def main():
    #setting up the display window
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    tfont = pygame.font.Font('freesansbold.ttf', 30)
    pygame.display.set_caption("The Solar System")
    
    #initializing the celestial bodies
    planets = make_objects()
    sun     = Planet(1.9890*pow(10, 30), 0, 0, 0, 0, YELLOW)
 
    #integration time
    dt = 43200  #seconds

    #setting up file for data output
    f = open("solar.dat", "w")
    #for planet in planets:
     #   f.write("%f\t%f\t%f\t%f\n" % (planet.x, planet.y, planet.vx. planet.vy))


    #main loop of the program
    i = 0
    while (i < 5000):
        for planet in planets:
            r  = math.sqrt(pow(sun.x-planet.x, 2) + pow(sun.y-planet.y, 2))
            rx = sun.x-planet.x
            ry = sun.y-planet.y

            axplanet = (G*sun.m)*(rx)/pow(r, 3)
            ayplanet = (G*sun.m)*(ry)/pow(r, 3)

            vxplanet = planet.vx + axplanet*dt
            vyplanet = planet.vy + ayplanet*dt

            xplanet = planet.x + vxplanet*dt
            yplanet = planet.y + vyplanet*dt
        
            planet.update(xplanet, yplanet, vxplanet, vyplanet)
            f.write("%f\t%f\t%f\t%f\n" % (planet.x, planet.y, planet.vx, planet.vy))

            pygame.draw.circle(window, sun.color, (int(sun.x*P2M) + WIDTH/2, int(sun.y*P2M) + HEIGHT/2), 25, 0)
            pygame.draw.circle(window, BLACK, (int(sun.x*P2M) + WIDTH/2, int(sun.y*P2M) + HEIGHT/2), 1, 0)
            pygame.draw.circle(window, planet.color, (int(planet.x*P2M + WIDTH/2), int(planet.y*P2M) + HEIGHT/2), 2, 0)

        t = str((i*dt)/86400)
        timestamp(t + " Days", tfont, window)
        i += 1
    
    f.close()
    time.sleep(10)
    
main()
