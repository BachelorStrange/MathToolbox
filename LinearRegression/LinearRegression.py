import matplotlib.pyplot as plt
import numpy as np
import math



def determinLinearRegressionParameters(x, y):
    averageX = CalculateAverage(x)
    averageY = CalculateAverage(y)
    sigmaX = CalculateStandardDeviation(x, averageX)
    sigmaY = CalculateStandardDeviation(y, averageY)
    print(averageX, averageY)
    print(sigmaX, sigmaY)
    cov = CalculateCovariance(x, averageX, y, averageY)
    print(cov)
    correlation = CalculateCorrelation(cov, sigmaX, sigmaY)
    print(correlation)
    slope = sigmaY/sigmaX * correlation
    axis_intersection = - sigmaY/sigmaX * correlation * averageX + averageY
    print(axis_intersection)
    print(slope)
    return slope, axis_intersection

def CalculateAverage(inputList):
    average = 0
    for i in range(len(inputList)):
        average += inputList[i]
    return average / len(inputList)

def CalculateStandardDeviation(inputList, average):
    sigma = 0
    for i in range(len(inputList)):
        sigma += (inputList[i] - average)**2
    sigma = sigma/len(inputList)
    return math.sqrt(sigma)

def CalculateCovariance(inputListX, averageX, inputListY, averageY):
    covariance = 0
    for i in range(len(inputListX)):
        covariance += (inputListX[i] - averageX) * (inputListY[i] - averageY)
    return covariance / (len(inputListX))

def CalculateCorrelation(covariance, deviationX, deviationY):
    return covariance/(deviationX * deviationY)
        

def plot():
    fig, ax = plt.subplots()
    ax.plot(x,y, 'o')
    xr = np.linspace(0, 10)
    yr = a * xr + b
    plt.plot(xr,yr, 'r')
    plt.show()


if __name__ == "__main__":
    input_tuples = [(2, 400), (4, 390), (3, 550), (0, 410), (5, 320), (2, 400), (1, 500), (7, 300), (3, 470), (8, 380)]
    x = [2, 4, 3, 0, 5, 2, 1, 7, 3, 8]
    y = [400, 390, 550, 410, 320, 400, 500, 300, 470, 380]
    a, b = determinLinearRegressionParameters(x, y)
    plot()