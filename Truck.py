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
        package.status = "en route"
        self.cargo.append(package)


