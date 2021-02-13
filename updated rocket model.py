import numpy as np
import matplotlib.pyplot as plt
from random import randrange

# initial conditions
distancefrommars = [0, 0, 500]
rocketposition = [0.1, 0.007, 0]
time = 0
rocketmovementvector = [-0.314, -0.314, 0.314]  # contains initial condition
B00 = [0, 0.2, -0.05]
B10 = [-0.5, 0.2, -0.5]
B01 = [0.15, -0.3, 1]
B11 = [-0.2, -0.3, -0.3]
yawpilotthreshold = 9  # how likely the pilot is to make a choice during each time step
pitchpilotthreshold = 9
choicelist = []
pathx = []
pathy = []
pathz = []
ax3d = plt.axes(projection="3d")
movementintime = [rocketmovementvector]

def decision(position, pilot):
    boolean = "B"
    if "pitch" in pilot:
        if position[0] < 0:
            boolean += "0"
        else:
            boolean += "1"
    else:
        boolean += "1"
    if "yaw" in pilot:
        if position[1] < 0:
            boolean += "0"
        else:
            boolean += "1"
    else:
        boolean += "1"
    return boolean


def howpilotsact(position):
    yawrand = randrange(10)
    pitchrand = randrange(10)
    if yawrand <= yawpilotthreshold:
        if pitchrand <= pitchpilotthreshold:
            return decision(position, "yawpitch")
        else:
            return decision(position, "yaw")
    else:
        if pitchrand <= pitchpilotthreshold:
            return decision(position, "pitch")
        else:
            return decision(position, "")


# running the simulation
while rocketposition[2] <= distancefrommars[2]:
    time += 1
    if rocketmovementvector[2] < 0:
        print("rocket stopped")
        break
    booleanchoice = howpilotsact(rocketmovementvector)
    choicelist.append(booleanchoice)
    if booleanchoice == "B00":
        rocketmovementvector = [rocketmovementvector[i] + B00[i] for i in range(len(rocketmovementvector))]
    elif booleanchoice == "B01":
        rocketmovementvector = [rocketmovementvector[i] + B01[i] for i in range(len(rocketmovementvector))]
    elif booleanchoice == "B10":
        rocketmovementvector = [rocketmovementvector[i] + B10[i] for i in range(len(rocketmovementvector))]
    elif booleanchoice == "B11":
        rocketmovementvector = [rocketmovementvector[i] + B11[i] for i in range(len(rocketmovementvector))]

    rocketposition = [rocketposition[i] + rocketmovementvector[i] for i in range(len(rocketmovementvector))]
    pathx.append(rocketposition[0])
    pathy.append(rocketposition[1])
    pathz.append(rocketposition[2])
    movementintime.append(rocketmovementvector)
## for i in choicelist:
#### do some analysis of choices here
print(time)
print(choicelist)

for i in movementintime:
    for x in i:
        print(x)
# plots 3d graph of the rocket's path
ax3d.plot3D(pathx, pathz, pathy)
plt.show()

timeaxis = np.linspace(0, time, num=time)

