import datetime

class Truck:
    def __init__(self, name, departure_time=None):
        self.name = name  # Truck name
        self.packages = []  # This will hold the list of package IDs assigned to the truck
        self.mileage = 0.0 # This keeps track of how far the truck has traveled in total
        self.time = departure_time if departure_time else datetime.timedelta(hours=8)  # Default 8:00 AM (when the truck begins deliveries)
                                                                                       # This lets each truck have different start time
        self.location = "4001 South 700 East"  # This sets the truck's starting location to the HUB
