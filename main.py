from Truck import Truck

truck1_package_list = [1, 13, 14, 15, 16, 19, 20, 26, 29, 30, 31, 34, 37, 40]
truck2_package_list = [4, 6, 7, 10, 11, 12, 17, 18, 21, 25, 28, 32, 36, 37, 38]
truck3_package_list = [2, 3, 5, 8, 9, 22, 23, 24, 27, 33, 35, 39]

truck1 = Truck("Truck#1", "", "4001 South 700 East", "", 0, 18, "08:00", 0)
truck1.load(1)
truck1.load(2)
truck1.load(3)

print(truck1.cargo)