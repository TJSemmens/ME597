# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1

import numpy as np
import math

class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[0 -4.0, 0.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        theta = goalPoint[2]
        return list((x, y, theta))

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
    
        pointList = []
        x = np.linspace(0, 2, 20)
        #y = x ** 2
        y = 1/(1+np.exp(-x))
        for i in range(len(x)):
            pointList.append([x[i], y[i]])
            


        pass
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        return pointList

