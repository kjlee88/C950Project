import distance_data
import loadPackageData


class Truck:
    def __init__(self, name, cargo, location, destination, total_mile, speed, start_time, elapsed_time):
        self.name = name
        self.cargo = cargo
        self.location = location
        self.destination = destination
        self.total_mile = total_mile
        self.speed = speed
        self.start_time = start_time
        self.elapsed_time = elapsed_time

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.name, self.cargo, self.location, self.destination, self.total_mile, self.speed, self.start_time, self.elapsed_time)

    def load(self, packageID):
        package = loadPackageData.myHash.get(packageID)
        package.status = "Loaded, at the hub"
        self.cargo.append(package)

