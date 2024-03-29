# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
nameList = ["circle", "line", "spiral"]
def plot_errors(filenames):
    count = 0
    for filename in filenames:
        headers, values=FileReader(filename).read_file() 
        # time_list=[]
        # first_stamp=values[0][-1]
        x= []
        y= []
        print(headers)
        for val in values:
            # time_list.append(val[-1] - first_stamp)
            x.append(val[0])
            y.append(val[1])


        plt.plot(x, y, label = nameList[count])
        count +=1
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend()
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title("odom x vs y")
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
