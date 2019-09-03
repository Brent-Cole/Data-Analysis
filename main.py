#import the packages to be used below
import matplotlib.pyplot as plt
import numpy as np


def main():
    # read in the file with the ht and wts
    infile = open("HT&WT2.txt")
    #initialize variables
    totalht = 0.0
    totalwt = 0.0
    i = 0
    name = []
    ht = []
    wt = []
    residual = []
    residualsum = 0.0

    #for the sake of efficiency I used the same for loop to do pretty much all my calculations all at once, instead of using multiple which might look prettier
    #reads in the index values into the name, hts into ht, and wts into wt, while also keeping track of total hts and wts to be used later
    #I also am calculating residuals based on the regression line choosen.
    for line in infile:
        temp = line.split('\t')
        name.append(int(temp[0]))
        ht.append(float(temp[1]))
        wt.append(float(temp[2]))
        totalht = totalht + float(temp[1])
        totalwt = totalwt + float(temp[2])
        residual.append(float(temp[2])-(6.134 * float(temp[1]) - 290))
        residualsum = residualsum + float(residual[i])
        i=i+1
    infile.close()

    #We have all the data now to perform the regression test finding mean height and weight
    #These values while not actively used in the coding were valuable on my paper while doing the math
    meanht= totalht/float(i)
    meanwt= totalwt/float(i)

    #Finding residual values
    median = np.median(residual)
    maximum = np.max(residual)
    minimum = np.min(residual)

    #Next I'll be calculating the Standard deviation
    std = np.std(wt)

    #Need to find the r value now
    r = np.corrcoef(ht,wt)

    #Printing the results to all the findings to the terminal
    print("Regression Line Equation: y = 6.134x - 290")
    print("Mean Ht: ", meanht)
    print("Mean Wt: ", meanwt)
    print("Median Residual: ", median)
    print("Maximum Residual: ", maximum)
    print("Minimum Residual: ", minimum)
    print("STD: ", std)
    print("r value: ", r)

    #I did the math on paper using the means above to get my regression line of y = 6.134x-290
    # At this point we have all the data put into three Python Lists so we can build our graph
    plt.scatter(ht,wt,s=.2,label="Data Points")
    x = np.linspace(62,74,4)
    y = 6.134 * x - 290
    plt.plot(x, y,'-g',label='Regression Line')

    #Formatting the graph so it looks good
    plt.xscale('linear')
    plt.yscale('linear')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.show()

main()
