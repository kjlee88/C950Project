import csv

import hash_table
import loadPackageData

with open('./CSVfiles/distanceCSV.csv') as distances:
    # Append each row to two-dimensional list
    distanceData = list(csv.reader(distances, delimiter=','))

with open('./CSVfiles/addressCSV.csv') as addresses:
    addressData = csv.reader(addresses)
    next(addressData)  # skip header
    addressList = []
    businessList = []
    for address in addressData:
        # Parse
        addressList.append(address[1])
        businessList.append(address[0])



    def lookup_address(address):
        index = (addressList.index(address))
        return index


    def get_distance(row, col):
        distance = distanceData[row][col]
        if distanceData[row][col] == "":
            distance = distanceData[col][row]

        print(distance)
        return distance







