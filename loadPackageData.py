# C950 - Webinar-2 - Getting Greedy, who moved my data?
# W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.

import csv
import math

from Package import Package
from hash_table import ChainingHashTable


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
            myHash.insert(pID, p)


# Hash table instance
myHash = ChainingHashTable()

# Load movies to Hash Table
loadPackageData('./CSVfiles/Package.csv')


# print(myHash.search())
# print("packages from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(myHash.table)):
#     print("Package: {}".format(myHash.search(i + 1)))  # 1 to 16 is sent to myHash.search()

# print(myHash.search(1))

# # Greedy Algorithm: Min Expenses => Max Profits
# def greedyAlgorithmMinExpenses(budget):
#     total = budget
#     c25dollar = 0
#     c10dollar = 0
#     c5dollar = 0
#     c1dollar = 0
#     while (budget >= 25):
#         if c25dollar > 3:  # why 3? 0,1,2,3 will not break so 4 times.
#             break
#         c25dollar += 1
#         budget = budget - 25
#     while (budget >= 10):
#         c10dollar += 1
#         budget = budget - 10
#     while (budget >= 5):
#         c5dollar += 1
#         budget = budget - 5
#     while (budget > 0):
#         if c1dollar > 3:
#             break
#         c1dollar += 1
#         budget = budget - 1
#
#     cDVDs = c25dollar + c10dollar + c5dollar + c1dollar
#
#     # expense calculation
#     eDVDs = 1.00 * cDVDs  # Material cost of DVD: $1.00
#     eLabor = 12.00 * (math.ceil(cDVDs / 10))  # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
#     eShipping = 0.50 * cDVDs  # Shipping cost is $0.50 per DVD
#     eTotal = eDVDs + eLabor + eShipping
#     profit = total - eTotal
#
#     print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total, cDVDs, eTotal, profit))
#     print(" {} x 25 dollar movie = ${:.2f}".format(c25dollar, c25dollar * 25.00))
#     print(" {} x 10 dollar movie = ${:.2f}".format(c10dollar, c10dollar * 10.00))
#     print(" {} x 5  dollar movie = ${:.2f}".format(c5dollar, c5dollar * 5.00))
#     print(" {} x 1  dollar movie = ${:.2f}".format(c1dollar, c1dollar * 1.00))
#
#
# print("\nGreedy Algorithm: Min Expenses => Max Profits")
# greedyAlgorithmMinExpenses(102)  # $102.00 budget
# greedyAlgorithmMinExpenses(94)  # $94.00 budget
# greedyAlgorithmMinExpenses(71)  # $71.00 budget
# greedyAlgorithmMinExpenses(200)  # $200.00 budget
