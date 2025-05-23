# Student ID: 012527055

from package import Package
from hashtable import HashTable
from distance_table import get_distance, address_list
from truck import Truck
from datetime import datetime, timedelta

# Step 1: Create hash table to store all packages
hash_table = HashTable()

# Step 2: Create and insert all 40 packages into the hash table
# Each package includes ID, address, deadline, city, zip, and weight
# These are added one by one into our custom hash table

package1 = Package(1, "195 W Oakland Ave", "10:30:00", "Salt Lake City", "84115", 21)
package2 = Package(2, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 44)
package3 = Package(3, "233 Canyon Rd", "EOD", "Salt Lake City", "84103", 2)
package4 = Package(4, "380 W 2880 S", "EOD", "Salt Lake City", "84115", 4)
package5 = Package(5, "410 S State St", "EOD", "Salt Lake City", "84111", 5)
package6 = Package(6, "3060 Lester St", "10:30:00", "West Valley City", "84119", 88)
package7 = Package(7, "1330 2100 S", "EOD", "Salt Lake City", "84106", 8)
package8 = Package(8, "300 State St", "EOD", "Salt Lake City", "84103", 9)
package9 = Package(9, "300 State St", "EOD", "Salt Lake City", "84103", 2)  # wrong address initially
package10 = Package(10, "600 E 900 South", "EOD", "Salt Lake City", "84105", 1)
package11 = Package(11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", "84118", 1)
package12 = Package(12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", "84119", 1)
package13 = Package(13, "2010 W 500 S", "10:30:00", "Salt Lake City", "84104", 2)
package14 = Package(14, "4300 S 1300 E", "10:30:00", "Millcreek", "84117", 88)
package15 = Package(15, "4580 S 2300 E", "09:00:00", "Holladay", "84117", 4)
package16 = Package(16, "4580 S 2300 E", "10:30:00", "Holladay", "84117", 88)
package17 = Package(17, "3148 S 1100 W", "EOD", "Salt Lake City", "84119", 2)
package18 = Package(18, "1488 4800 S", "EOD", "Salt Lake City", "84123", 6)
package19 = Package(19, "177 W Price Ave", "EOD", "Salt Lake City", "84115", 37)
package20 = Package(20, "3595 Main St", "10:30:00", "Salt Lake City", "84115", 37)
package21 = Package(21, "3595 Main St", "EOD", "Salt Lake City", "84115", 3)
package22 = Package(22, "6351 South 900 East", "EOD", "Murray", "84121", 2)
package23 = Package(23, "5100 South 2700 West", "EOD", "Salt Lake City", "84118", 5)
package24 = Package(24, "5025 State St", "EOD", "Murray", "84107", 7)
package25 = Package(25, "5383 South 900 East #104", "10:30:00", "Salt Lake City", "84117", 7)
package26 = Package(26, "5383 South 900 East #104", "EOD", "Salt Lake City", "84117", 25)
package27 = Package(27, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 5)
package28 = Package(28, "2835 Main St", "EOD", "Salt Lake City", "84115", 7)
package29 = Package(29, "1330 2100 S", "10:30:00", "Salt Lake City", "84106", 2)
package30 = Package(30, "300 State St", "10:30:00", "Salt Lake City", "84103", 1)
package31 = Package(31, "3365 S 900 W", "10:30:00", "Salt Lake City", "84119", 1)
package32 = Package(32, "3365 S 900 W", "EOD", "Salt Lake City", "84119", 1)
package33 = Package(33, "2530 S 500 E", "EOD", "Salt Lake City", "84106", 1)
package34 = Package(34, "4580 S 2300 E", "EOD", "Holladay", "84117", 2)
package35 = Package(35, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104", 88)
package36 = Package(36, "2300 Parkway Blvd", "10:30:00", "West Valley City", "84119", 88)
package37 = Package(37, "410 S State St", "10:30:00", "Salt Lake City", "84111", 2)
package38 = Package(38, "410 S State St", "EOD", "Salt Lake City", "84111", 9)
package39 = Package(39, "2010 W 500 S", "EOD", "Salt Lake City", "84104", 9)
package40 = Package(40, "380 W 2880 S", "10:30:00", "Salt Lake City", "84115", 45)

# Insert each package into the hash table using the package ID as the key
for i in range(1, 41):
    hash_table.insert(i, locals()[f"package{i}"])

# Apply special delivery constraints
# Packages delayed until 9:05 AM
for pid in [6, 25, 28, 32]:
    hash_table.lookup(pid).available_time = datetime.strptime("09:05", "%H:%M").time()

# Assign packages to trucks
# Truck 1: Earliest packages and coupled deliveries
truck1_packages = [
    1,   # 10:30 deadline
    13,  # 10:30 deadline
    14,  # must be delivered with ID: 15, 19
    15,  # 9:00 deadline (must leave first)
    16,  # must be delivered with ID: 13, 19
    19,  # Same route as others
    20,  # 10:30 deadline, must be delivered with ID: 13, 15
    29,  # 10:30 deadline
    30,  # 10:30 deadline
    31,  # 10:30 deadline
    34,  # Same address as 15/16
    37,  # 10:30 deadline
    40   # 10:30 deadline
]

# Truck 2: Can depart after 9:05
truck2_packages = [
    3,   # EOD, can only be on truck 2
    6,   # 10:30 deadline (shows at depot at 9:05)
    18,  # EOD, can only be on truck 2
    25,  # 10:30 deadline (shows at depot at 9:05)
    26,  # Same address as 25
    28,  # EOD (shows at depot at 9:05)
    32,  # EOD, (shows at depot at 9:05)
    36,  # 10:30 deadline/ can only be on truck 2
    38,  # EOD, can only be on truck 2
    39   # EOD
]

# Truck 3: Leaves after 10:20
truck3_packages = [
    2,   # EOD
    4,   # EOD
    5,   # EOD
    7,   # EOD
    8,   # EOD
    9,   # wrong address corrected at 10:20
    10,  # EOD
    11,  # EOD
    12,  # EOD
    17,  # EOD
    21,  # EOD
    22,  # EOD
    23,  # EOD
    24,  # EOD
    27,  # EOD
    33,  # EOD
    35   # EOD
]

# Create trucks with starting times
truck1 = Truck("Truck 1", timedelta(hours=8))
truck2 = Truck("Truck 2", timedelta(hours=9, minutes=5))
truck3 = Truck("Truck 3", timedelta(hours=10, minutes=20))

truck1.packages = truck1_packages.copy()
truck2.packages = truck2_packages.copy()
truck3.packages = truck3_packages.copy()

# Function to fix package 9's address after 10:20am
def update_package9_address(current_time):
    if current_time >= datetime.strptime("10:20", "%H:%M").time():
        package9 = hash_table.lookup(9)
        if package9.address != "410 S State St":
            package9.address = "410 S State St"
            package9.zip = "84111"

# Nearest neighbor delivery algorithm
# Delivers as much as possible up to the current time
def deliver_packages_up_to(truck, end_time):
    current_location = "4001 South 700 East"
    for package_id in truck.packages:
        package = hash_table.lookup(package_id)
        package.start_time = truck.time
        package.truck_number = truck.name
    while truck.packages and (datetime.min + truck.time).time() <= end_time:
        nearest_package = None
        shortest_distance = float('inf')
        nearest_address = None

        for package_id in truck.packages:
            package = hash_table.lookup(package_id)

            # Skip delayed packages not yet arrived at the hub
            if hasattr(package, "available_time") and (datetime.min + truck.time).time() < package.available_time:
                continue

            distance = get_distance(current_location, package.address)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_package = package
                nearest_address = package.address

        for package_id in list(truck.packages):
            package = hash_table.lookup(package_id)
            if package.address == nearest_address:
                travel_time = timedelta(hours=shortest_distance / 18)
                truck.time += travel_time
                truck.mileage += shortest_distance
                package.status = "Delivered"
                package.delivery_time = (datetime.min + truck.time).time()
                truck.packages.remove(package_id)

        current_location = nearest_address

def deliver_all_packages():
    deliver_packages_up_to(truck1, datetime.strptime("23:59", "%H:%M").time())
    deliver_packages_up_to(truck2, datetime.strptime("23:59", "%H:%M").time())
    deliver_packages_up_to(truck3, datetime.strptime("23:59", "%H:%M").time())


# Runs deliveries up to a specific time
def run_deliveries_until(time_obj):
    update_package9_address(time_obj)

    if time_obj >= datetime.strptime("08:00", "%H:%M").time():
        deliver_packages_up_to(truck1, time_obj)
    if time_obj >= datetime.strptime("09:05", "%H:%M").time():
        deliver_packages_up_to(truck2, time_obj)
    if time_obj >= datetime.strptime("10:20", "%H:%M").time():
        deliver_packages_up_to(truck3, time_obj)

# Convert string to time
def convert_time_str(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Use HH:MM (24-hour clock).")
        return None

# Print all packages at a time
def print_status_of_all_packages(time_obj):
    print(f"\nPackage Statuses at {time_obj.strftime('%H:%M')}:")
    for package_id in range(1, 41):
        package = hash_table.lookup(package_id)

        if package.delivery_time and package.delivery_time <= time_obj:
            status = f"Delivered at {package.delivery_time.strftime('%H:%M')}"
        elif hasattr(package, "available_time") and time_obj < package.available_time:
            status = "Delayed – Not Yet Arrived"
        elif package.start_time and (datetime.min + package.start_time).time() <= time_obj:
            status = "En Route"
        else:
            status = "At Hub"

        print(f"Package ID: {package.package_id} | Address: {package.address} | Deadline: {package.deadline} | Truck: {package.truck_number} | Status: {status}")

# Print one package at a time
def print_status_of_single_package(package_id, time_obj):
    package = hash_table.lookup(package_id)

    if package.delivery_time and package.delivery_time <= time_obj:
        status = f"Delivered at {package.delivery_time.strftime('%H:%M')}"
    elif hasattr(package, "available_time") and time_obj < package.available_time:
        status = "Delayed – Not Yet Arrived"
    elif package.start_time and (datetime.min + package.start_time).time() <= time_obj:
        status = "En Route"
    else:
        status = "At Hub"

    print(f"\nPackage ID: {package.package_id} | Address: {package.address} | Deadline: {package.deadline} | Truck: {package.truck_number} | Status at {time_obj.strftime('%H:%M')}: {status}")


# User menu
def show_menu():
    while True:
        print("\nWGUPS Delivery Tracking Menu")
        print("1. View ALL package statuses at a specific time")
        print("2. View ONE package status at a specific time")
        print("3. View TOTAL mileage")
        print("4. Exit")

        choice = input("\nEnter option (1-4): ").strip()

        if choice == "1":
            time_input = input("Enter time (HH:MM): ")
            time_obj = convert_time_str(time_input)
            if time_obj:
                run_deliveries_until(time_obj)
                print_status_of_all_packages(time_obj)

        elif choice == "2":
            pkg_id = int(input("Enter package ID (1-40): "))
            time_input = input("Enter time (HH:MM): ")
            time_obj = convert_time_str(time_input)
            if time_obj:
                run_deliveries_until(time_obj)
                print_status_of_single_package(pkg_id, time_obj)


        elif choice == "3":
            deliver_all_packages()  # Run all deliveries before totaling mileage
            total = truck1.mileage + truck2.mileage + truck3.mileage
            print(f"\nTotal mileage traveled by all trucks: {total:.1f} miles")


        elif choice == "4":
            print("Program exited.")
            break

        else:
            print("Invalid selection. Please choose 1-4.")

# Launch program
show_menu()