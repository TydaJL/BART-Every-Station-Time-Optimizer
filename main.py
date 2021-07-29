#Importing Libraries
from array import *
from datetime import datetime
from datetime import timedelta

#Array of All Lines

lines = ["r", "b", "o", "g", "y"]

#Initializing First 5 Train Times for All Lines
r_S = [["5:00", "5:11", "5:26", "5:41", "5:56"], ["6:20", "6:30", "6:45", "7:00", "7:15"]] #Richmond > Millbrae
r_N = [["6:23", "6:38", "6:53", "7:08", "7:23"], ["7:40", "7:55", "8:10", "8:25", "8:40"]] #Millbrae > Richmond
b_W = [["5:06", "5:21", "5:36", "5:51", "6:06"], ["6:10", "6:25", "6:40", "6:55", "7:10"]] #Dublin/Pleasanton > Daly City
b_E = [["5:12", "5:27", "5:42", "5:57", "6:12"], ["6:16", "6:31", "6:46", "7:01", "7:16"]] #Daly City > Dublin/Pleasanton
o_N = [["4:59", "5:14", "5:29", "5:44", "5:59"], ["6:20", "6:35", "6:50", "7:05", "7:20"]] #Berryessa/North San Jose > Richmond
o_S = [["5:03", "5:18", "5:33", "5:48", "6:03"], ["6:26", "6:40", "6:55", "7:10", "7:25"]] #Richmond > Berryessa/North San Jose
y_W = [["4:47", "5:02", "5:17", "5:32", "5:47"], ["6:28", "6:43", "6:58", "7:13", "7:28"]] #Antioch > SFO
y_E = [["5:11", "5:26", "5:41", "5:56", "6:11"], ["6:35", "6:50", "7:05", "7:20", "7:35"]] #SFO > Antioch
g_W = [["4:40", "4:55", "5:10", "5:25", "5:40"], ["6:03", "6:18", "6:33", "6:48", "7:03"]] #Berryessa/North San Jose > Daly City
g_E = [["6:05", "6:20", "6:35", "6:50", "7:05"], ["7:29", "7:44", "7:59", "8:14", "8:29"]] #Daly City > Berryessa/North San Jose

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
            tDelta = timedelta(hours=int(timestampArray[row][col].split(':')[0]), minutes=int(timestampArray[row][col].split(':')[1]))
            minutesAfterMidnight = int(tDelta.total_seconds() / 60)
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
    lowestTime = timeList[0]
    for i in range(len(timeList)):
        if(timeList[i]) < lowestTime:
            lowestTime = timeList[i]
    print(lowestTime)


def printAllLines():
    print(lineList)

#Testing Cases

#convertIntoMinutes(r_S, r_SConvertedMinutes)
#convertIntoMinutes(b_W, b_WConvertedMinutes)

convertAllIntoMinutes(lineList)
timeToComplete(r_NConvertedMinutes, r_NTime)
alltimeToComplete(completeTime)
print(r_NConvertedMinutes)
print(r_NTime)
lowestTimeToComplete(r_NTime)
print(completeTime)
#print(lineList)
#print(convertedList)



#for row in range(len(r)):
#    for col in range(len(r[row])):
#        rConvertedMinutes[row][col] = timedelta(hours = r[row][col], minutes ) j

# print(rConvertedMinutes)