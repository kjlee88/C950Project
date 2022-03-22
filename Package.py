class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, mass, notes, start_timestamp, delivery_timestamp, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.start_timestamp = start_timestamp
        self.deliver_timestamp = delivery_timestamp
        self.status = status

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" %(self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.mass, self.notes, self.start_timestamp, self.delivery_timestamp, self.status)

