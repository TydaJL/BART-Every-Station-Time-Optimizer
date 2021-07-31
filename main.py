#Importing Libraries
from array import *
from datetime import datetime
from datetime import timedelta

#Array of All Lines

lines = ["r", "b", "o", "g", "y"]

#Initializing First 5 Train Times for All Lines
r_S = [["5:00 AM", "5:11 AM", "5:26 AM", "5:41 AM", "5:56 AM"], ["6:20 AM", "6:30 AM", "6:45 AM", "7:00 AM", "7:15 AM"]] #Richmond > Millbrae
r_N = [["6:23 AM", "6:38 AM", "6:53 AM", "7:08 AM", "7:23 AM"], ["7:40 AM", "7:55 AM", "8:10 AM", "8:25 AM", "8:40 AM"]] #Millbrae > Richmond
b_W = [["5:06 AM", "5:21 AM", "5:36 AM", "5:51 AM", "6:06 AM"], ["6:10 AM", "6:25 AM", "6:40 AM", "6:55 AM", "7:10 AM"]] #Dublin/Pleasanton > Daly City
b_E = [["5:12 AM", "5:27 AM", "5:42 AM", "5:57 AM", "6:12 AM"], ["6:16 AM", "6:31 AM", "6:46 AM", "7:01 AM", "7:16 AM"]] #Daly City > Dublin/Pleasanton
o_N = [["4:59 AM", "5:14 AM", "5:29 AM", "5:44 AM", "5:59 AM"], ["6:20 AM", "6:35 AM", "6:50 AM", "7:05 AM", "7:20 AM"]] #Berryessa/North San Jose > Richmond
o_S = [["5:03 AM", "5:18 AM", "5:33 AM", "5:48 AM", "6:03 AM"], ["6:26 AM", "6:40 AM", "6:55 AM", "7:10 AM", "7:25 AM"]] #Richmond > Berryessa/North San Jose
y_W = [["4:47 AM", "5:02 AM", "5:17 AM", "5:32 AM", "5:47 AM", "6:00 AM", "6:17 AM", ], ["6:28 AM", "6:43 AM", "6:58 AM", "7:13 AM", "7:28 AM"]] #Antioch > SFO
y_E = [["5:11 AM", "5:26 AM", "5:41 AM", "5:56 AM", "6:11 AM"], ["6:35 AM", "6:50 AM", "7:05 AM", "7:20 AM", "7:35 AM"]] #SFO > Antioch
g_W = [["4:40 AM", "4:55 AM", "5:10 AM", "5:25 AM", "5:40 AM"], ["6:03 AM", "6:18 AM", "6:33 AM", "6:48 AM", "7:03 AM"]] #Berryessa/North San Jose > Daly City
g_E = [["6:05 AM", "6:20 AM", "6:35 AM", "6:50 AM", "7:05 AM"], ["7:29 AM", "7:44 AM", "7:59 AM", "8:14 AM", "8:29 AM"]] #Daly City > Berryessa/North San Jose

r_SConvertedMinutes = [[0 for numRow in range(len(r_S[0]))] for numCol in range(len(r_S))]
r_NConvertedMinutes = [[0 for numRow in range(len(r_N[0]))] for numCol in range(len(r_N))]
b_WConvertedMinutes = [[0 for numRow in range(len(b_W[0]))] for numCol in range(len(b_W))]
b_EConvertedMinutes = [[0 for numRow in range(len(b_E[0]))] for numCol in range(len(b_E))]
o_NConvertedMinutes = [[0 for numRow in range(len(o_N[0]))] for numCol in range(len(o_N))]
o_SConvertedMinutes = [[0 for numRow in range(len(o_S[0]))] for numCol in range(len(o_S))]
y_WConvertedMinutes = [[0 for numRow in range(len(y_W[0]))] for numCol in range(len(y_W))]
y_EConvertedMinutes = [[0 for numRow in range(len(y_E[0]))] for numCol in range(len(y_E))]
g_WConvertedMinutes = [[0 for numRow in range(len(g_W[0]))] for numCol in range(len(g_W))]
g_EConvertedMinutes = [[0 for numRow in range(len(g_E[0]))] for numCol in range(len(g_E))]

r_STime = [0 for numRow in range(len(r_S[0]))]
r_NTime = [0 for numRow in range(len(r_N[0]))]
b_WTime = [0 for numRow in range(len(b_W[0]))]
b_ETime = [0 for numRow in range(len(b_E[0]))]
o_NTime = [0 for numRow in range(len(o_N[0]))]
o_STime = [0 for numRow in range(len(o_S[0]))]
y_WTime = [0 for numRow in range(len(y_W[0]))]
y_ETime = [0 for numRow in range(len(y_E[0]))]
g_WTime = [0 for numRow in range(len(g_W[0]))]
g_ETime = [0 for numRow in range(len(g_E[0]))]



lineList = [r_S, r_N, b_W, b_E, o_N, o_S, y_W, y_E, g_W, g_E]
convertedList = [r_SConvertedMinutes, r_NConvertedMinutes, b_WConvertedMinutes, b_EConvertedMinutes, o_NConvertedMinutes, o_SConvertedMinutes, y_WConvertedMinutes, y_EConvertedMinutes, g_WConvertedMinutes, g_EConvertedMinutes]
completeTime = [r_STime, r_NTime, b_WTime, b_ETime, o_NTime, o_STime, y_WTime, y_ETime, g_WTime, g_ETime]
timeToCompleteLine = [0 for i in range(len(lineList))]

x = 0

#for row in range(len(r_S)):
#    for col in range(len(r_S[row])):
#        x += 1
#print(r_S)

#Converting Times into Minutes
def convertIntoMinutes(timestampArray, convertedIntoMinutesArray): #timestamp Array is r, b, o, g, y; convertedIntoMinutesArray is rConvertedMinutes, etc.
    for row in range(len(timestampArray)):
        for col in range(len(timestampArray[row])):
            tDelta = timedelta(hours=int(timestampArray[row][col].split(':')[0]), minutes=int(timestampArray[row][col].split(':')[1].strip(" APM")))
            minutesAfterMidnight = int(tDelta.total_seconds() / 60)
            if " PM" in timestampArray[row][col]:
                minutesAfterMidnight += 720
            convertedIntoMinutesArray[row][col] = minutesAfterMidnight

def convertAllIntoMinutes(allList):
    for i in range(len(lineList)):
        convertIntoMinutes(lineList[i], convertedList[i])

def timeToComplete(lineMinutesList, timeList):
    for i in range(len(lineMinutesList[0])):
        timeList[i] = lineMinutesList[1][i] - lineMinutesList[0][i]

def alltimeToComplete(allTimesList):
    for i in range(len(completeTime)):
        timeToComplete(convertedList[i], completeTime[i])


def lowestTimeToComplete(timeList):
    return min(timeList)

def lowestTimeAllLines():
    time = 0
    for i in range(len(completeTime)):
        time += lowestTimeToComplete(completeTime[i])
        
    print("The lowest possible time to ride all stations of BART is " + str(time) + " minutes.")



def printAllLines():
    print(lineList)