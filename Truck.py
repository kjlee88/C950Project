import distance_data
import loadPackageData


class Truck:
    def __init__(self, name, cargo, location, destination, total_mile, speed, start_time, elapsed_time):
        self.name = name
        self.cargo = cargo
        self.location = location
        self.destination = destination
        self.totalMile = total_mile
        self.speed = speed
        self.start_time = start_time
        self.elapsed_time = elapsed_time

        self.cargo = []

        print("{0} was created.".format(self.name))

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.name, self.cargo, self.location, self.destination, self.total_mile, self.speed, self.start_time, self.elapsed_time)

    def load(self, packageID):
        package = loadPackageData.myHash.search(packageID)
        package.status = "Loaded, at the hub"
        self.cargo.append(package)

# 3, 8, 30, 18, 36, 37, 38, 5, 9, 12
# 14, 15, 19, 13, 16, 20

truck1_package_list = [13, 39, 27, 35, 4, 40, 20, 21, 19, 14, 15, 16, 34]
truck2_package_list = [3, 8, 30, 18, 36, 37, 38, 5, 9, 12, 23, 11, 18, 10]
truck3_package_list = [1, 28, 2, 33, 7, 29, 17, 6, 31, 22, 24, 25, 26]

# print(len(truck1_package_list))

truck1 = Truck("Truck#1", "", "4001 South 700 East", "", 0, 18, "08:00", 0)
truck2 = Truck("Truck#2", "", "4001 South 700 East", "", 0, 18, "09:05", 0)
truck3 = Truck("Truck#3", "", "4001 South 700 East", "", 0, 18, "10:20", 0)

for i in truck1_package_list:
    truck1.load(i)


for i in truck2_package_list:
    truck2.load(i)


for i in truck3_package_list:
    truck3.load(i)



# for i in range(len(truck3.cargo)):
#      print("Package ID: " + str(truck3.cargo[i].ID) + " Deadline: " + truck3.cargo[i].deadline)


# print(truck1.cargo[0].address)

def deliveryAlgo(truck):
    current_location = truck.location
    distance_pair = {}
    sorted_package_list = []
    # sort the cargo by closest next location
    # get the distance from starting location to each package location
    for pkg in range(len(truck.cargo)):
        distance_pair[truck.cargo[pkg].ID] = distance_data.get_distance(distance_data.lookup_address(current_location), distance_data.lookup_address(truck.cargo[pkg].address))


    for pair in range(len(distance_pair)):
        key_list = list(distance_pair.keys())
        value_list = list(distance_pair.values())
        position = value_list.index(min(value_list))
        sorted_package_list.append(key_list[position])
        del distance_pair[key_list[position]]

    return sorted_package_list
    # min_dist = min(distance_list[1])
    # min_pkgID =
    # print(min_dist)

    # for p1 in distance_list:
    #     min_dist = 100000000
    #     min_name = ''
    #
    #     for p2 in distance_list:
    #         if p1[0] == p2[0]:
    #             continue
    #
    #         dist = abs(p1[1] - p2[1])
    #
    #         if min_dist > dist:
    #             min_dist = dist
    #             min_name = p2[0]
    #
    # sorted_package_list.append( [p1[0], min_name, min_dist] )
    # return sorted_package_list


        # return arranged_distance_list
# print(truck1.cargo[0].ID)
print(deliveryAlgo(truck1))
    # for i in range(len(truck.cargo)):
    #     min_distance = min(distance_list)
    #     arranged_package_list.append(truck.cargo[distance_list.index(min_distance)])
    #     distance_list.remove(min_distance)
    #
    # return arranged_package_list

# for i in range(len(deliveryAlgo(truck1))):
#     print(deliveryAlgo(truck1)[i])

# print(deliveryAlgo(truck1)[1])

# deliveryAlgo(truck1)
# print(truck1.deadlineList)