from math import atan2, asin, sqrt, pi

M_PI=3.1415926535

class Logger:
    
    def __init__(self, filename, headers=["e", "e_dot", "e_int", "stamp"]):
        
        self.filename = filename

        with open(self.filename, 'w') as file:
            
            header_str=""

            for header in headers:
                header_str+=header
                header_str+=", "
            
            header_str+="\n"
            
            file.write(header_str)


    def log_values(self, values_list):

        with open(self.filename, 'a') as file:
            
            vals_str=""
            
            for value in values_list:
                vals_str+=f"{value}, "
            
            vals_str+="\n"
            
            file.write(vals_str)
            

    def save_log(self):
        pass

class FileReader:
    def __init__(self, filename):
        
        self.filename = filename
        
        
    def read_file(self):
        
        read_headers=False

        table=[]
        headers=[]
        with open(self.filename, 'r') as file:

            if not read_headers:
                for line in file:
                    values=line.strip().split(',')

                    for val in values:
                        if val=='':
                            break
                        headers.append(val.strip())

                    read_headers=True
                    break
            
            next(file)
            
            # Read each line and extract values
            for line in file:
                values = line.strip().split(',')
                
                row=[]                
                
                for val in values:
                    if val=='':
                        break
                    row.append(float(val.strip()))

                table.append(row)
        
        return headers, table
    
    

# TODO Part 3: Implement the conversion from Quaternion to Euler Angles
def euler_from_quaternion(quat):
    """
    Convert quaternion (w in last place) to euler roll, pitch, yaw.
    quat = [x, y, z, w]
    """
    siny_cosp = 2*(quat.w*quat.z+quat.x*quat.y)
    cosy_cosp = 1 - 2*(quat.y*quat.y + quat.z*quat.z)
    yaw = atan2(siny_cosp, cosy_cosp)
    # just unpack yaw
    return yaw


#TODO Part 4: Implement the calculation of the linear error
def calculate_linear_error(current_pose, goal_pose):
    print(current_pose)    
    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y,theta]
    # Remember to use the Euclidean distance to calculate the error.
    x_current, y_current = current_pose[:2]
    x_goal, y_goal = goal_pose[:2]

    error_linear= ((x_goal - x_current) ** 2 + (y_goal - y_current) ** 2) ** 0.5
    
    return error_linear

#TODO Part 4: Implement the calculation of the angular error
def calculate_angular_error(current_pose, goal_pose):

    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y,theta]
    # Remember that this function returns the difference in orientation between where the robot currently faces and where it should face to reach the goal
    
    current_x, current_y = current_pose[:2]
    goal_x, goal_y = goal_pose[:2]
    error_angular = atan2(goal_y - current_y, goal_x - current_x) - current_pose[2]
    # error_angular = goal_pose[2] - current_pose[2]
    print(error_angular)
    error_angular = (error_angular + pi) % (2 * pi) - pi #I'm taking the modulo of 0 to 2*pi but shifting it by pi in either direction so its -pi to pi


    # Remember to handle the cases where the angular error might exceed the range [-π, π]

    ...
    
    return error_angular
