from __future__ import division, print_function
from visual import *
from visual.graph import *

#VP03.1.0 Fan Cart Code
# scene.width = 800
# scene.y = 400
# vgraph = gcurve(color=color.green)
#
# track = box(pos=vector(0,-0.05,0), length=2.0, height=0.03, width=0.10, color=color.white)
# cart = box(pos=vector(0,0,0), length=0.1, height=0.06, width=0.06, color=color.cyan)
# m_cart = 0.8
# p_cart = m_cart * vector(0.2,0,0)
# delta_t = 0.01
# t=0

#VP03.2.0 Motion with Zero Net Force
# scene.width = 800
# scene.y = 400
# vgraph = gcurve(color=color.green)
#
# track = box(pos=vector(0,-0.05,0), length=2.0, height=0.03, width=0.10, color=color.white)
# cart = box(pos=vector(-0.95,0,0), length=0.1, height=0.06, width=0.06, color=color.cyan)
# m_cart = 0.8
# p_cart = m_cart * vector(0.2,0,0)
# delta_t = 0.01
# t=0
#
# while t < 12:
#      rate(100)
#      cart.pos = cart.pos + p_cart * delta_t
#      t = t + delta_t
#      vgraph.plot(pos=(t, p_cart.x))
#
# print('time')
# print(t)
# print('velocity')
# print(p_cart / m_cart)

#VP03.3.0 Motion with a Constant Net Force
# scene.width = 800
# scene.y = 400
# vgraph = gcurve(color=color.magenta)
#
# track = box(pos=vector(0,-0.05,0), length=2.0, height=0.03, width=0.10, color=color.white)
# cart = box(pos=vector(-0.95,0,0), length=0.1, height=0.06, width=0.06, color=color.cyan)
# m_cart = 0.8
# p_cart = m_cart * vector(0.2,0,0)
# delta_t = 0.01
# t=0
#
# F_net = vector(0.0525,0,0)
#
# while t < 6:
#      rate(100)
#      cart.pos = cart.pos + p_cart * delta_t
#      t = t + delta_t
#      vgraph.plot(pos=(t, p_cart.x))
#
#      p_cart = p_cart + F_net * delta_t
#
# print('time')
# print(t)
# print('velocity')
# print(p_cart / m_cart)

#VP03.4
scene.width = 800
scene.y = 400
vgraph = gcurve(color=color.magenta)

track = box(pos=vector(0,-0.05,0), length=2.0, height=0.03, width=0.10, color=color.white)
cart = box(pos=vector(-0.95,0,0), length=0.1, height=0.06, width=0.06, color=color.cyan)
m_cart = 0.8
p_cart = m_cart * vector(0.2,0,0)
delta_t = 0.01
t=0

F_net = vector(-0.0083,0,0)

while t < 35:
     rate(100)
     cart.pos = cart.pos + p_cart * delta_t
     t = t + delta_t
     vgraph.plot(pos=(t, p_cart.x))

     p_cart = p_cart + F_net * delta_t

print('time')
print(t)
print('velocity')
print(p_cart / m_cart)