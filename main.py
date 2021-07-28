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

r_SConvertedMinutes = [[0 for numRow in range(len(r_S[0]))] for numCol in range(len(r_S))]
b_WConvertedMinutes = [[0 for numRow in range(len(b_W[0]))] for numCol in range(len(b_W))]
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

#Testing Cases

convertIntoMinutes(r_S, r_SConvertedMinutes)
convertIntoMinutes(b_W, b_WConvertedMinutes)
print(r_SConvertedMinutes)
print(b_WConvertedMinutes)


#for row in range(len(r)):
#    for col in range(len(r[row])):
#        rConvertedMinutes[row][col] = timedelta(hours = r[row][col], minutes ) j

# print(rConvertedMinutes)