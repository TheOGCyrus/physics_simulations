
from __future__ import division, print_function
from visual import *
from visual.graph import *

scene.width = scene.height = 800
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
mMoon = 7e22
#mMoon = 0 # change  when answer questions!!!
deltat = 60
#deltat = 9000 #- changing delta t
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6,
               color=color.yellow, make_trail=True)
Moon = sphere(pos=Earth.pos + vector(4e8,0,0), radius = 1.75e6, color = color.white)

#vcraft = vector(0, 2e3, 0) #original orbit
#vcraft = vector(0, 3.285e3, 0) #moon crash
#vcraft = vector(0, 3.325e3, 0) #eliptical around both Earth and Moon
vcraft = vector(0, 3.2735e3, 0) #figure 8
#vcraft = vector(0,3.4e3,0) #interesting result 1
#vcraft = vector(0, 3.27e3, 0) #part 4 given velocity

pcraft = mcraft*vcraft
t=0
scene.autoscale = False ##turn off automatic camera zoom


sf = 1.5
sff = 2e4 #change this based on orbit
parrow = arrow(pos=vector(craft.pos), axis=sf * pcraft, color=color.green, shaftwidth = 1500000)
Farrow = arrow(pos=vector(craft.pos), axis=(0,0,0), color=color.red, shaftwidth = 1500000)


#Vp08
kineticenergy = gcurve(color = color.cyan,dot=True)
potentialenergy = gcurve(color = color.green,dot=True)
kplusu = gcurve(color = color.yellow,dot=True)
K = 0
U = 0

 

while t < 365*24*60*60:
    #rate(100)
    rate(1e4) #sped up rate

    rE = craft.pos - Earth.pos
    if mag(rE) < Earth.radius:
        break  ## exit from the loop
    F_grav_E = G * (mEarth * mcraft) / mag(rE) ** 2 * (-norm(rE))
    rM = craft.pos - Moon.pos
    if mag(rM) < Moon.radius:
        break  ## exit from the loop
    F_grav_M = G * (mMoon * mcraft) / mag(rM) ** 2 * (-norm(rM))
    F_net = F_grav_E + F_grav_M

    pcraft = pcraft + F_net * deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat

    parrow.pos = craft.pos
    parrow.axis = pcraft * sf

    Farrow.pos = craft.pos
    Farrow.axis = F_net * sff

    scene.center = (Earth.pos + Moon.pos) / 2

    #vp08-calculations
    K = (mag(pcraft) **2) /(2*mcraft)
    U = -G*(mcraft*mEarth)/mag(rE) - G*(mcraft*mMoon)/mag(rM)

    #enery vs time
    kineticenergy.plot(pos = (t,K))
    potentialenergy.plot(pos = (t,U))
    kplusu.plot(pos = (t,K+U))
    
   # #energy vs seperation
   #  kineticenergy.plot(pos = (mag(rE),K))
   #  potentialenergy.plot(pos = (mag(rE),U))
   #  kplusu.plot(pos = (mag(rE),K+U))
    
    t = t+deltat
    
    
    
            
    

    
