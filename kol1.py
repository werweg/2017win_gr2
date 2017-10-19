###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#! /usr/bin/env python2.7
import random

#first value
mu=90
sigma=20
angle=random.gauss(mu, sigma)

#turbulence value in every iteration
turbulence_mu=0
turbulence_sigma=2
def getTurbulence():
	return random.gauss(turbulence_mu, turbulence_sigma)

print "First orientation: " + str(angle)
#90 degrees is desired value

while True:
	correction=(90-angle)*0.5
	angle+=correction
	angle+=getTurbulence()
	print "Orientation: " + str(angle)

