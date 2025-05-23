# This class defines what a Package is and what information it holds
class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight, status="At the hub", delivery_time=None):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.delivery_time = delivery_time
        self.start_time = None
        self.delivery_time = None
        self.truck_number = None
# This method tells Python how to print the package details in a readable way
def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, "
                f"City: {self.city}, Zip: {self.zip_code}, Weight: {self.weight}kg, "
                f"Status: {self.status}, Delivered at: {self.delivery_time}")




