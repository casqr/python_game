#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:43:01 2017

@author: kaswan
"""

import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Verlet Simple Cloth System')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Particle:
    def __init__(self, x, y, m = 1.0):
        self.m = m
        self.x = x
        self.y = y
        self.oldx = x
        self.oldy = y
        self.newx = x
        self.newy = y
        self.ax = 0
        self.ay = 9.8
        
    def update(self, delta_t):
        # Verlet Integration
        self.newx = 2.0 * self.x - self.oldx + self.ax * delta_t * delta_t 
        self.newy = 2.0 * self.y - self.oldy + self.ay * delta_t * delta_t 
        self.oldx = self.x
        self.oldy = self.y
        self.x = self.newx
        self.y = self.newy
        
        # Collision Process
        if self.x < 0 or self.x > WIDTH:
            self.x, self.oldx = self.oldx, self.x
        if self.y < 0 or self.y > HEIGHT:
            self.y, self.oldy = self.oldy, self.y

    def draw(self, surf, size):
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), size)
        
class Constraint:
    def __init__(self, index0, index1):
        self.index0 = index0
        self.index1 = index1
        delta_x = particles[index0].x - particles[index1].x
        delta_y = particles[index0].y - particles[index1].y
        self.restLength = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        
    def update(self):
        delta_x = particles[self.index1].x - particles[self.index0].x
        delta_y = particles[self.index1].y - particles[self.index0].y
        deltaLength = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        diff = (deltaLength - self.restLength)/deltaLength

        if self.index0 != 0 and self.index0 != NUM_X -1:
            particles[self.index0].x += 0.5 * diff * delta_x
            particles[self.index0].y += 0.5 * diff * delta_y
        if self.index1 != 0 and self.index1 != NUM_X -1:
            particles[self.index1].x -= 0.5 * diff * delta_x
            particles[self.index1].y -= 0.5 * diff * delta_y
            
    def draw(self, surf, size):
        x0 = particles[self.index0].x
        y0 = particles[self.index0].y
        x1 = particles[self.index1].x
        y1 = particles[self.index1].y
        pygame.draw.line(surf, WHITE, (int(x0), int(y0)), (int(x1), int(y1)), size)
            
delta_t = 0.1
NUM_ITER = 10

# create particles
NUM_X = 10
NUM_Y = 10
particles = []
for j in range(NUM_Y):
    for i in range(NUM_X):
        x = 100 + i * 20.0
        y = j * 20.0
        p = Particle(x, y)
        particles.append(p)

constraints = []
for j in range(NUM_Y):
    for i in range(NUM_X):
        if i < (NUM_X - 1):
            index0 = i + j * NUM_X
            index1 = (i + 1) + j * NUM_X
            c = Constraint(index0, index1)
            constraints.append(c)
        if j < (NUM_Y - 1):
            index0 = i + j * NUM_X
            index1 = i + (j + 1) * NUM_X
            c = Constraint(index0, index1)
            constraints.append(c)

while True:
    screen.fill(BLACK)

    # particles update
    for i in range(len(particles)):
        if i == 0 or i == NUM_X -1:
            continue
        particles[i].update(delta_t)

    # particles draw
    for i in range(len(particles)):
        particles[i].draw(screen, 3)

    # constraints update
    for i in range(NUM_ITER):
        for ii in range(len(constraints)):
            constraints[ii].update()

    # constraints draw
    for i in range(len(constraints)):
        constraints[i].draw(screen, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)