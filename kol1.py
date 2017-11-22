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

class Plane_position():

    def __init__(self):
        self.mu = 90
        self.sigma = 20
        self.angle = random.gauss(self.mu, self.sigma)

    def __str__(self):
        return '%s %f' % ('Current angle: ', self.angle)

    def get_angle(self):
        return self.angle

    def update_angle(self, diff):
        self.angle += diff


class Flight():

    def __init__(self):
        self.position = Plane_position()
        self.turbulence_mu = 0
        self.turbulence_sigma = 2
        self.correction_fraction = 0.5
        self.desired_angle = 90

    def add_correction(self):
        correction = (self.desired_angle - self.position.get_angle())*self.correction_fraction
        self.position.update_angle(correction)

    def add_turbulence(self):
        turbulence = random.gauss(self.turbulence_mu, self.turbulence_sigma)
        self.position.update_angle(turbulence)

    def single_step(self):
        time.sleep(1)
        self.add_correction()
        self.add_turbulence()
        print self.position

    def simulation(self):
        while True:
            self.single_step()


if __name__ == "__main__":

    flight = Flight()
    flight.simulation()
