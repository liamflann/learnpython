# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:59:14 2016

@author: Liam
"""

#This is for the drake equation

name = raw_input("What is your name? ")

def Drake():
    print """The Drake equation estimates the number of civilizations that may
    exist in our galaxy and may be able to communiticate with us. It is
    based on a few parameters:
                1. R: rate of star creation (aprox 7)
                2. p: percentage of stars with planets (approx 40%)
                3. n: the average number of planets that could support life for
                    each star with planets.
                4. f: percent of those that develop life (approx 13%)
                5. i: the percent that goes on to develop intelligent life.
                6. c: percentage willing and able to communicate with us.
                7. L: expected life of civilizations
            As you can see, not all of these have values associated with them.
            That's where you come in. You will assign values to the uknowns."""
    ready = raw_input("Ready? Yes/No: ")
    if "Yes" in ready:
            print "Great!"
    else:
        print "Too bad!"
    print "Okay, now I need your input."
    R = 7.0
    p = .40
    n = float(raw_input("n: "))
    f = .13
    i_in = float(raw_input("i (do not include %): "))
    i = i_in/100
    c_in = float(raw_input("c (do not include %): "))
    c = c_in/100
    L = float(raw_input("L: "))
    eqn = R*p*n*f*i*c*L
    print "From your values, we would expect about " , eqn, " civilizations exist."
    
    
    