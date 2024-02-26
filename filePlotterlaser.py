# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
import numpy
markerList = ["o", "^","s"]
colorList = ["blue", "orange", "grey"]
nameList = ["circle", "line", "spiral"]
def plot_errors(filenames):
    count = 0
    for filename in filenames:
        headers, values=FileReader(filename).read_file() 
        # time_list=[]
        # first_stamp=values[0][-1]
        currentAngle = 0
        incrementAngle = 0.5*numpy.pi/180
        x = []
        y = []
        for val in values:
            val.pop()
            for range in val:
                # print(range)
                x.append(numpy.cos(currentAngle)*range)
                y.append(numpy.sin(currentAngle)*range)
                currentAngle+= incrementAngle

                plt.scatter(x, y, marker=markerList[count], c= colorList[count])
        count+=1



    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend(nameList, labelcolor = colorList)
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.title("laser reflection(1st snapshot)")
    plt.grid()
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    # for filename in filenames:
    plot_errors(filenames)
