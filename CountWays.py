class CountWays():
    calculatedSteps = {0:1}

    def countWay(self, numSteps, stepSizeList = [1,2,3]):
        stepSizeList.sort()
        counter = 0

        if numSteps in self.calculatedSteps:
            return self.calculatedSteps[numSteps]

        for step in stepSizeList:
            if numSteps >= step:
                counter += self.countWay(numSteps - step, stepSizeList)
            else:
                break

        self.calculatedSteps[numSteps] = counter
        return counter

if __name__ == "__main__":
    o = CountWays()
    print(o.countWay(100, stepSizeList= [1,2,3,7,11]))
