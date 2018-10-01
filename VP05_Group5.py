from __future__ import division, print_function
from visual import *

scene.width = scene.height = 800
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6,
               color=color.yellow, make_trail=True)
#vcraft = vector(0,2e3,0) #original velocity for orbit
#vcraft = vector(0, 3.55e3, 0) #attempting to break from orbit
#vcraft = vector(0, 2e3, 0) #circular orbit
vcraft = vector(0, 3e3, 0) #elliptical orbit
pcraft = mcraft*vcraft
r = craft.pos - Earth.pos
t=0
scene.autoscale = False ##turn off automatic camera zoom

#print(pcraft)

sf = 1/3
sff = 3e4 #change this based on orbit
parrow = arrow(pos=vector(craft.pos), axis=sf * pcraft, color=color.green, shaftwidth = 1500000)
Farrow = arrow(pos=vector(craft.pos), axis=(0,0,0), color=color.red, shaftwidth = 1500000)

while t < 10*365*24*60*60:
    rate(100)
    #rate(1e5) #sped up rate
    if mag(r) < Earth.radius:
        break  ## exit from the loop

    r = craft.pos - Earth.pos
    F_grav = G * (mEarth * mcraft) / mag(r) ** 2
    F_net = F_grav * -norm(r)

    pcraft = pcraft + F_net * deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat

    parrow.pos = craft.pos
    parrow.axis = pcraft * sf

    Farrow.pos = craft.pos
    Farrow.axis = F_net * sff

    t = t+deltat