# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
import numpy
def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file() 
    # time_list=[]
    # first_stamp=values[0][-1]
    print(headers)
    currentAngle = 0
    incrementAngle = 0.5*numpy.pi/180
    x = []
    y = []
    for val in values:
        val.pop()
        for range in val:
            print(range)
            x.append(numpy.cos(currentAngle)*range)
            y.append(numpy.sin(currentAngle)*range)
            currentAngle+= incrementAngle
            print(currentAngle)
    print(x)


    plt.scatter(x, y)
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    # plt.legend()
    plt.grid()
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)
