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


    def get_distance(current_location, destination):
        current_location = lookup_address(current_location)
        destination = lookup_address(destination)
        distance = distanceData[current_location][destination]
        if distanceData[current_location][destination] == "":
            distance = distanceData[destination][current_location]

        return float(distance)