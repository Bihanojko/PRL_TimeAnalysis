import subprocess


TIME_VARIANTS = {'real': 1, 'user': 2, 'sys': 3}


# CHANGE
ITERATION_COUNT = 10
WANTED_TIME = TIME_VARIANTS['real']
# CHANGE


testSet = [
    ["300000", "4"],
    ["500000", "4"],
    ["700000", "4"],
    ["1000000", "4"],
    ["1500000", "4"],
    ["2000000", "4"],
    ["2500000", "4"],
    ["3250000", "4"],
    ["4000000", "4"],
    ["5000000", "4"],
]


def strToSeconds(timeStamp):
    minutes = int(timeStamp[:timeStamp.find('m')])
    seconds = float(timeStamp[timeStamp.find('m') + 1:timeStamp.find('s')])
    return minutes * 60 + seconds


# Preparing file takes the longest
for testData in testSet:
    subprocess.check_output(["dd",
                             "if=/dev/random",
                             "bs=1",
                             "count=" + testData[0],
                             "of=numbers" + testData[0]])

elapsedTimes = [0] * ITERATION_COUNT
for testData in testSet:
    output = subprocess.check_output(["cp", "numbers" + testData[0], "numbers"])
    for i in range(ITERATION_COUNT):
        output = subprocess.check_output(["./test.sh",
                                          testData[0],
                                          testData[1]],
                                         stderr=subprocess.STDOUT).decode('utf-8').split("\n")
        elapsedTimes[i] = strToSeconds(output[WANTED_TIME][4:])
    averageTime = sum(elapsedTimes) / float(ITERATION_COUNT)
    print("{0} {1}".format(testData[0], averageTime))

# Clean up after yourself
output = subprocess.check_output(["rm", "numbers*"])
