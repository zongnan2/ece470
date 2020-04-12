ball = sim.getObjectHandle('Sphere2')
sim.setObjectFloatParameter(ball,3001,0.5) -- y direction velocity
sim.setObjectFloatParameter(ball,3002,0.35) -- z direction velocity
sim.switchThread()
