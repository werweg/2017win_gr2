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
import time

class Flight():
	def __init__(self):
		self.mu=90
		self.sigma=20

		self.turbulence_mu=0
		self.turbulence_sigma=2

		self.angle=random.gauss(self.mu, self.sigma)
		self.desired_angle=90
		self.correction_fraction=0.5

	def addCorrection(self):
		correction=(self.desired_angle-self.angle)*self.correction_fraction
		self.angle+=correction

	def addTurbulence(self):
		self.angle+=random.gauss(self.turbulence_mu, self.turbulence_sigma)

	def simulation(self):
		print '%s %f'%('Initial angle: ', self.angle)
		while True:
			time.sleep(1)
			self.addCorrection()
			self.addTurbulence()
			print '%s %f'%('Corrected angle: ', self.angle)


flight=Flight()
flight.simulation()
