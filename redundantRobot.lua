-- if you wish to execute code contained in an external file instead,
-- use the require-directive, e.g.:
--
-- require 'myExternalFile'
--
-- Above will look for <V-REP executable path>/myExternalFile.lua or
-- <V-REP executable path>/lua/myExternalFile.lua
-- (the file can be opened in this editor with the popup menu over
-- the file name)

function sysCall_threadmain()
    -- Put some initialization code here
    sphere = sim.getObjectHandle("Sphere2")
    target = sim.getObjectHandle("redundantRob_target")
    velocity = 3
    delaytime = 20
    sensor = sim.getObjectHandle('Proximity_sensor0')
    initial_pos = sim.getObjectPosition(target,-1)

    -- Put your main loop here, e.g.:
    --
    while sim.getSimulationState()~=sim.simulation_advancing_abouttostop do
        result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector = sim.readProximitySensor(sensor)
        if (result>0) then
            position = sim.getObjectPosition(sphere,-1)
            sim.addStatusbarMessage(position[2])
            linear_v,angular_v = sim.getObjectVelocity(sphere)
            position[1] = position[1]+linear_v[1]*sim.getSimulationTimeStep()
            position[2] = position[2]+linear_v[2]*sim.getSimulationTimeStep()
            position[3] = position[3]+linear_v[3]*sim.getSimulationTimeStep()
            sim.addStatusbarMessage(position[2])
            sim.moveToPosition(target,-1,position,nil,velocity)
        end
        --sim.moveToPosition(target,-1,initial_pos,nil,velocity)


    --     local p=sim.getObjectPosition(objHandle,-1)
    --     p[1]=p[1]+0.001
    --     sim.setObjectPosition(objHandle,-1,p)
    --     sim.switchThread() -- resume in next simulation step
    end

end

function sysCall_cleanup()
    -- Put some clean-up code here
end


-- ADDITIONAL DETAILS:
-- -------------------------------------------------------------------------
-- If you wish to synchronize a threaded loop with each simulation pass,
-- enable the explicit thread switching with
--
-- sim.setThreadAutomaticSwitch(false)
--
-- then use
--
-- sim.switchThread()
--
-- When you want to resume execution in next simulation step (i.e. at t=t+dt)
--
-- sim.switchThread() can also be used normally, in order to not waste too much
-- computation time in a given simulation step
-- -------------------------------------------------------------------------
