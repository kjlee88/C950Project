import csv
import math

import hash_table
from Package import Package


def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNotes = package[7]
            if pNotes == "":
                pNotes = "N/A"
            pStatus = "At the hub"


            # movie object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)

            # insert it into the hash table
            myHash.add(pID, p)


# Hash table instance
myHash = hash_table.HashMap()

# Load movies to Hash Table
loadPackageData('./CSVfiles/Package.csv')