# Author KYUNG JUN LEE (Student ID: 000979601)

import datetime
import time

import distance_data
import hash_table
import loadPackageData

hashmap = loadPackageData.myHash

# Create 3 trucks (truck name, cargo list, starting location, destination, elapsed mile, speed (miles per minute), delivery start time, elapsed time)
from Truck import Truck

# truck1 = Truck("Truck#1", [], "4001 South 700 East", "", 0, 0.3, [8, 0, 0], 0)
truck1 = Truck("Truck#1", [], "4001 South 700 East", "", 0, 0.3, "8:00", 0)
truck2 = Truck("Truck#2", [], "4001 South 700 East", "", 0, 0.3, "9:05", 0)
truck3 = Truck("Truck#3", [], "4001 South 700 East", "", 0, 0.3, "10:13", 0)

hashmap.get(9).address = "410 S State St"

# Packages to be loaded to each truck by Package ID
truck1_package_list = [13, 39, 27, 35, 4, 40, 20, 21, 19, 14, 15, 16, 34, 29, 1]
truck2_package_list = [3, 8, 30, 18, 36, 37, 38, 5, 12, 23, 11, 10, 31, 32, 6]
truck3_package_list = [28, 2, 33, 7, 17, 22, 24, 25, 26, 9]

# Load the truck
for i in truck1_package_list:
    truck1.load(i)

for i in truck2_package_list:
    truck2.load(i)

for i in truck3_package_list:
    truck3.load(i)


# Determine truck's route. Compares distances to possible destinations, and chooses the closest destination.
def closest_route(truck):
    current_location = truck.location
    distance_pair = {}
    address_list = [current_location]
    copy_of_cargo = []

    # sort the cargo by closest next location
    # get the distance from starting location to each package location
    for pkg in range(len(truck.cargo)):
        copy_of_cargo.append(truck.cargo[pkg])
        distance_pair[truck.cargo[pkg].ID] = distance_data.get_distance(current_location, truck.cargo[pkg].address)

    for pair in range(len(distance_pair)):
        key_list = list(distance_pair.keys())  # keys = package IDs
        value_list = list(distance_pair.values())  # values = distance from current location
        position = value_list.index(min(value_list))  # position of the minimum distance

        package = loadPackageData.myHash.get(
            key_list[position])  # calling package by package ID that corresponds to minimum distance
        address_list.append(package.address)  # adding that package to the new list

        current_location = package.address
        del distance_pair[key_list[position]]

        truck.cargo.remove(package)

        for pkg in range(len(truck.cargo)):
            distance_pair[truck.cargo[pkg].ID] = distance_data.get_distance(current_location, truck.cargo[pkg].address)

    sorted_address_list = []

    # Removes duplicate destinations
    for i in address_list:
        if i not in sorted_address_list:
            sorted_address_list.append(i)

    sorted_address_list.append("4001 South 700 East")  # returning to the hub location

    return sorted_address_list  # final destination list for given truck


def delivery_simulation(truck, route):
    if not truck1.cargo:
        for i in truck1_package_list:
            truck1.load(i)

    if not truck2.cargo:
        for i in truck2_package_list:
            truck2.load(i)

    if not truck3.cargo:
        for i in truck3_package_list:
            truck3.load(i)

    elapsed_mile = 0
    elapsed_time = datetime.datetime.strptime(truck.start_time, '%H:%M')
    # elapsed_time = datetime.datetime(100, 1, 1, truck.start_time[0], truck.start_time[1], truck.start_time[2])
    delivered_cargo = []

    for i in range(len(truck.cargo)):
        # loadPackageData.myHash.get(truck.cargo[i]).timestamp = elapsed_time
        truck.cargo[i].start_timestamp = elapsed_time.time()

    for i in range(len(route) - 1):
        truck.destination = route[i + 1]
        traveled_dist = distance_data.get_distance(truck.location, truck.destination)
        elapsed_mile += traveled_dist
        elapsed_time += datetime.timedelta(minutes=round(traveled_dist / truck.speed))
        elapsed_time2 = elapsed_time.time()
        for i, elem in enumerate(truck.cargo):
            if truck.destination == elem.address:
                delivered_cargo.append(elem.ID)
                package = loadPackageData.myHash.get(elem.ID)
                package.status = "delivered"
                package.delivery_timestamp = (elapsed_time2)
        if delivered_cargo:
            truck.location = truck.destination
            print(truck.name + " delivered Package: " + str(delivered_cargo) + " at " + truck.location + " at " + str(
                elapsed_time2) + ". Elapsed Distance= " + "{:0.2f}".format(elapsed_mile) + " mi")
        else:
            truck.location = truck.destination
            print(truck.name + " has returned to the Hub at " + str(
                elapsed_time2) + ". \nTotal distance traveled by " + truck.name + " = " + "{:0.2f}".format(
                elapsed_mile) + " mi")
            truck.total_mile = elapsed_mile
        delivered_cargo.clear()


def findTotalMile():
    return truck2.total_mile + truck1.total_mile + truck3.total_mile

# delivery_simulation(truck1, closest_route(truck1))
# print("\n")
# delivery_simulation(truck2, closest_route(truck2))
# print("\n")
# delivery_simulation(truck3, closest_route(truck3))
# print("\n")
# print("Total Distance Traveled by All Trucks: " + str(findTotalMile()) + " miles")
# print("\n")
# print(loadPackageData.myHash.get(1).start_timestamp)
# print(loadPackageData.myHash.get(1).delivery_timestamp)
# print(loadPackageData.myHash.get(1).status)

class Main:
    delivery_simulation(truck1, closest_route(truck1))
    print("\n")
    delivery_simulation(truck2, closest_route(truck2))
    print("\n")
    delivery_simulation(truck3, closest_route(truck3))
    print("\n")
    print("Total Distance Traveled by All Trucks: " + str(findTotalMile()) + " miles")
    print("\n")

    print("WGUPS DELIVERY SIMULATION PROGRAM")
    print("WRITTEN BY KYUNG JUN LEE")

    user_input = input("""
    Select an option to begin:
        1. Run delivery simulation again and find the total mileage traveled by all trucks
        2. Get all package information at a particular time
    """)

    if user_input == '1':
        delivery_simulation(truck1, closest_route(truck1))
        print("\n")
        delivery_simulation(truck2, closest_route(truck2))
        print("\n")
        delivery_simulation(truck3, closest_route(truck3))
        print("\n")
        print("Total Distance Traveled by All Trucks: " + str(findTotalMile()) + " miles")
    elif user_input == '2':
        input_time = input('Enter a time in HH:MM format: ')
        user_time = datetime.datetime.strptime(input_time, '%H:%M').time()
        address_correction_time = datetime.datetime.strptime("10:20", '%H:%M').time()
        for p in range(1,41):
            delivery_start_time = loadPackageData.myHash.get(p).start_timestamp
            delivered_time = loadPackageData.myHash.get(p).delivery_timestamp

            if user_time < address_correction_time:
                hashmap.get(9).address = "300 State St"

            if user_time < delivery_start_time:
                loadPackageData.myHash.get(p).status = "at the hub"
            elif (user_time >= delivery_start_time) and (user_time < delivered_time):
                loadPackageData.myHash.get(p).status = "en route"
            elif user_time >= delivered_time:
                loadPackageData.myHash.get(p).status = "delivered @ " + str(delivered_time)

            print("Package ID: " + str(hashmap.get(p).ID) + " | Delivery Address: " + hashmap.get(p).address + " | Delivery Deadline: " + hashmap.get(p).deadline + " | City: " + hashmap.get(p).city + " | Zip Code: " + hashmap.get(p).zipcode + " | Package Wt: " + hashmap.get(p).mass + " | Status: " + hashmap.get(p).status)
