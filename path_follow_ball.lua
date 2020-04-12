path = sim.getObjectHandle('Path')
ball = sim.getObjectHandle('Sphere1')
pathlength = sim.getPathLength(path)
posOnPath = 0
v = 0.1
while true do

    l = posOnPath/pathlength
    if (l>pathlength) then
        l = pathlength
    end

    position = sim.getPositionOnPath(path,l)
    orientation = sim.getOrientationOnPath(path,l)

    position[1] = 0.7


    sim.setObjectPosition(ball,-1,position)
    sim.setObjectOrientation(ball,-1,orientation)

    posOnPath = posOnPath + v*sim.getSimulationTimeStep()

    sim.switchThread()
end
