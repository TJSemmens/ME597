from math import atan2, asin, sqrt

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

            # TODO Part 5: Write the values from the list to the file

            for val in values_list:
                vals_str += str(val)
                vals_str += ", "
            
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
            # Skip the header line

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
                    replacers = {"[":"", "]" : "", ")":""}
                    for symbol, space in replacers.items():
                        val = val.replace(symbol, space)
                    if val=='':
                        break
                    
                    try:
                        if val == " inf":
                            # row.append(0)
                            continue
                        else:
                            row.append(float(val.strip()))
                    except:
                        continue
                table.append(row)
        
        return headers, table


# TODO Part 5: Implement the conversion from Quaternion to Euler Angles
def euler_from_quaternion(quat):
    """
    Convert quaternion (w in last place) to euler roll, pitch, yaw.
    quat = [x, y, z, w]
    """
    yaw = atan2(2*(quat.w*quat.z+quat.x*quat.y), 1 - 2*(quat.y**2 + quat.z**2))
    return yaw


