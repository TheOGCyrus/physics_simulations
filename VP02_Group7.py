from __future__ import division, print_function
from visual import *

##n = 0
##num = 22

##while n <= 10:
##    num = num - 2
##    n = n + 1
##    print(num)

##print('end of program')

# ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.green)
# block = box(pos=vector(-8,0,0), color=color.yellow)
# velocity = vector(0.4, 0.6, 0)
# delta_t = 0.1
# t=0
#
# while t < 12:
#     rate(100)
#     ball.pos = ball.pos + velocity * delta_t
#     t = t + delta_t

wall = box(pos=vector(0,4,-0.5), length=20, height=10, width=0.1, color=color.green)
#particle = sphere(pos=vector(-10,0,0), radius = 0.5, color=color.magenta)
#velocity = vector(0.5,0,0)
delta_t = 0.1
t=0

# while t < 40:
#     rate(100)
#     particle.pos = particle.pos + velocity * delta_t
#     t = t + delta_t
#
# print(t)

particle = sphere(pos=vector(-10,-1,0), radius = 0.5, color=color.magenta)
velocity = vector(0.5,0.25,0)
while t < 40:
     rate(100)
     particle.pos = particle.pos + velocity * delta_t
     t = t + delta_t

print(t)