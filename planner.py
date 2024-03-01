# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0, 0.0]):
        
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
        for i in range(0,2,0.4):
            x= i
            #y=x^2
            y= i^2
            #y = 1/(1+e^(-x))
            #y = 1/(1+math.exp(-i))
            pointList.append([x,y])


        pass
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        return pointList

