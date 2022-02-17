import random
import memory_profiler
from time_profiler import timer

def genElements(minVal, maxVal, amount):

    #Generate list of unique random numbers
    try:
        eleList = random.sample(range(minVal, maxVal), amount)
    except ValueError:
        print("Not enough numbers to complete range.")

    #Make two elements in the list the same value
    randVal = eleList[random.randint(0, amount)]
    randPos = eleList[random.randint(0, amount)]
    if eleList[randPos] == randVal:
        eleList[randPos+1] = randVal
    else:
        eleList[randPos] = randVal
    # eleList = []
    # randVal = random.randint(minVal,maxVal)
    # randPos1 = random.randint(0,amount)
    # randPos2 = random.randint(0,amount)
    # for i in range(amount):
    #     if i == randPos1 or i == randPos2:
    #         eleList.append(randVal)
    #     randInt = random.randint(minVal,maxVal)
    #     while randInt not in eleList:
    #         eleList.append((randInt))
        # if randInt in eleList:
        #     pass
        # else:
        #     eleList.append(randInt)
    return eleList

@timer()
def SCAN(list):
    listLen = len(list)
    for i in range(listLen - 1):
        for j in range(i + 1, listLen):
            if list[i] == list[j]:
                print(i, " - ", j)
                print(list[i])
                return
            else:
                continue

@timer()
#@profile
def STOR(list):
    listLen = len(list)
    emptyList = [0] * listLen
    for i in range(listLen):
        if emptyList[list[i]] == 1:
            print("Duplicate at i = ", i)
            print(list[i])
            return
        else:
            emptyList[list[i]] = 1

@timer()
#@profile
def STOR1(list):
    # testList = []
    # for i in range(0, len(list)):
    #     if list[i] not in testList:
    #         testList.append(list[i])
    #     else:
    #         print("Duplicate at i = ", i)
    #         print(list[i])


    testList = set()
    for i in list:
        if i in testList:
            print("Duplicate at i = ", i)
            print(list[i])
        testList.add(i)

    return


# print(genElements(0,1000000,1000000))
randomList = genElements(0, 2000000, 2000000)
print(randomList)
SCAN(randomList)
STOR(randomList)
STOR1(randomList)