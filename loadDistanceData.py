import csv

def loadDistanceData(fileName):
    with open(fileName) as distances:
        # Append each row to two-dimensional list
        distanceData = list(csv.reader(distances, delimiter=','))

    # to find number of rows
    # print(len(distanceData))

    # to find number of cols
    # print(len(distanceData[0]))

    # distanceDataflipped = (list(zip(*distanceData)))


# Load distance file
loadDistanceData('./CSVfiles/distanceCSV.csv')


# def loadAddressData()