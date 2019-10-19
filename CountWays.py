calculatedSteps = {0:1}

def countWay(numSteps, stepSizeList = [1,2,3]):
    stepSizeList.sort()
    counter = 0

    if numSteps in calculatedSteps:
        return calculatedSteps[numSteps]

    for step in stepSizeList:
        if numSteps >= step:
            counter += countWay(numSteps - step, stepSizeList)
        else:
            return counter

    calculatedSteps[numSteps] = counter
    return counter

print(countWay(100, stepSizeList= [1,2,3,7,11]))
