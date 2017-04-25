#John Binzer
#Euler Method for 2 body gravitational system
#
# Used to approximate the solution of the initial value problem
#             y'=f(t, y)  on interval  [a, b]  with initial condition   y(a) = alpha
# at N+1 spaced intervals

def euler(a, b, N, alpha, f):
    #a and b are endpoints, N is the step size, alpha is the initial condition and f is an array that contains
    #the constants to determine the function [m, rx, r]
    h = (b-a)/N
    t = a
    w = alpha
    print "(%d, %d)" % (t,w)

    for i in range(1,N):
        w = w + h * (G*f[0]*rx)/pow(r, 3)
        t = a + i*h
        print "(%d, %d)" % (t, w)

euler(1, 4, 10, 0, [)
