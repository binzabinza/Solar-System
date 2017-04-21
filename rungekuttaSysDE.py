#!/usr/bin/env python

'''
John Binzer

Runge-Kutta Method for Systems of Differential Equations

!!!PROGRAMMED FOR A SYSTEM OF TWO EQUATIONS!!!
'''

import sys

def rungekuttaSysDE(a, b, m, N, alpha):
    #a, b are endpoints
    #m is an array containing the different equations
    #N determines the step size
    #alpha is an array containing the intial conditions

    l = length(m)
    e = 2.7182818284590452353602874713527

    h = (b-a)/N
    t = a

    for j in range(l):
        w[j] = alpha(j)

    print("t(%d) = %g", a, w)
    

    for i in range(N):
        for j in range(l):
            f = m(j)
            k[0, j] = h*f(t, w(0), w(1))
        for j in range(l):
            f = m(j)
            k[1, j] = h*f(t+h/2, w(0)+k(0,0)/2, w(1)+k(0, 1)/2)
        for j in range(l):
            f = m(j)
            k[2, j] = h*f(t+h/2, w(0)+k(1, 0)/2, w(1)+k(1, 1)/2)
        for j in range(l):
            f = m(j)
            k[3, j] = h*f(t+h, w(0)+k(2, 0), w(1)+k(2, 1))

        for j in range(l):
            w[j] = w(j) + (k(0, j-1) + 2 * k(1, j-1)+ 2 * k(2, j-1) + k(3, j-1))/6

        t = a+i*h

        print("t(%d) = %g", t, w)
