# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import dinningRecord

days = []

def getDays():
    global days
    days = dinningRecord.giveDays()

def sortUsage(days):
    xAxis = []
    yAxis = []
    counter = 0
    for day in days:
        if day != -1:
            xAxis.append(counter)
            yAxis.append(day)
        counter += 1
    both = [xAxis, yAxis]
    return both
    
def calculateLSA(xy):
    global days
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXX = 0
    for x in xy[0]:
        sumX += x
        sumXX += x*x
    #print("sumX: " + str(sumX))
    #print("sumXX: " + str(sumXX))

    for y in xy[1]:
        sumY += y
    #print("sumY: " + str(sumY))
    
    for a in range(0, len(xy[0])):
        sumXY += xy[0][a]*xy[1][a]
    #print("sumXY: " + str(sumXY))
    
    one = (len(xy[0]) * sumXY)
    two = sumX * sumY
    three = one - two
    four = len(xy[0]) * sumXX
    five = sumX**2
    six = four - five
    slope = three / six
    #print("FINAL: " + str(slope))
    
    one = sumY - (slope * sumX)
    b = one / len(xy[0])
    #print(b)
    
    twoPointsX = [0,len(days)]
    twoPointsY = [b,(slope*len(days) + b)]
    
    extraMoney = twoPointsY[1]
    print("\nExtra money: " + str(extraMoney))
    
    lastDayAdded = xy[0][len(xy[0])-1]
    
    moneyPerDay = days[lastDayAdded] / (len(days) - lastDayAdded)
    print("\nNeeded Money Per Day: " + str(moneyPerDay))
    
    mb = [twoPointsX, twoPointsY]
    return mb
    
def plotData(xy, mb):
    plt.plot(xy[0], xy[1], 'o')
    plt.plot(mb[0], mb[1], 'g')
    plt.axis([0, len(days), 0, 1500])
    plt.ylabel('Money')
    plt.xlabel('Time')
    plt.show()

if __name__ == "__main__":
    getDays()
    #print(len(days))
    xy = sortUsage(days)
    
    mb = calculateLSA(xy)   
    
    plotData(xy, mb)
    
