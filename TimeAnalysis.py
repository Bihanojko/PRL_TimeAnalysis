import subprocess


TIME_VARIANTS = {'real': 2, 'user': 3, 'sys': 4}


# CHANGE
ITERATION_COUNT = 10
WANTED_TIME = TIME_VARIANTS['real']
# CHANGE


testSet = [
    ["10", "4"],
    ["20", "4"],
    ["30", "4"],
    ["40", "4"],
    ["50", "4"],
    ["60", "4"],
    ["70", "4"],
    ["80", "4"],
    ["90", "4"],
    ["100", "4"],
    ["110", "4"],
    ["120", "4"],
    ["130", "4"],
    ["140", "4"],
    ["150", "4"],
    ["160", "4"],
    ["170", "4"],
    ["180", "4"],
    ["190", "4"],
    ["200", "4"],
    ["210", "4"],
    ["220", "4"],
    ["230", "4"],
    ["240", "4"],
    ["250", "4"],
    ["260", "4"],
    ["270", "4"],
    ["280", "4"],
    ["290", "4"],
    ["300", "4"],
    ["310", "4"],
    ["320", "4"],
    ["330", "4"],
    ["340", "4"],
    ["350", "4"],
    ["360", "4"],
    ["370", "4"],
    ["380", "4"],
    ["390", "4"],
    ["400", "4"],
    ["500", "4"],
    ["600", "4"],
    ["700", "4"],
    ["800", "4"],
    ["900", "4"],
    ["1000", "4"]
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
        output = subprocess.check_output(["./test.sh", testData[0], testData[1]], stderr=subprocess.STDOUT).decode('utf-8').split("\n")
        elapsedTimes[i] = strToSeconds(output[int(testData[0]) + WANTED_TIME][4:])
    averageTime = sum(elapsedTimes) / float(ITERATION_COUNT)
    print("{0} {1}".format(testData[0], averageTime))

# Clean up after yourself
output = subprocess.check_output(["rm", "numbers*"])
