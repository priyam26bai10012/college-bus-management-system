from file_manager import load_data, save_data, get_next_id
from validators import required_text, positive_integer, read_id, find_by_id


class BusManager:
    filename = "buses.json"

    def __init__(self):
        self.buses = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.buses)

    def add_bus(self):
        print("\nAdd Bus")
        number = required_text("Bus number: ")
        driver = required_text("Driver name: ")
        capacity = positive_integer("Capacity: ")

        if any(b["number"].lower() == number.lower() for b in self.buses):
            print("A bus with this number already exists.")
            return

        bus = {
            "id": get_next_id(self.buses),
            "number": number,
            "driver": driver,
            "capacity": capacity
        }
        self.buses.append(bus)
        self.save()
        print("Bus added successfully.")

    def view_buses(self):
        if not self.buses:
            print("No buses found.")
            return
        print("\nID | Bus No | Driver | Capacity")
        print("-" * 45)
        for b in self.buses:
            print(f'{b["id"]} | {b["number"]} | {b["driver"]} | {b["capacity"]}')

    def update_bus(self):
        bus_id = read_id("Enter bus ID: ")
        bus = find_by_id(self.buses, bus_id)
        if not bus:
            print("Bus not found.")
            return

        driver = input(f'Driver [{bus["driver"]}]: ').strip()
        capacity = input(f'Capacity [{bus["capacity"]}]: ').strip()

        if driver:
            bus["driver"] = driver
        if capacity:
            try:
                capacity = int(capacity)
                if capacity <= 0:
                    raise ValueError
                bus["capacity"] = capacity
            except ValueError:
                print("Invalid capacity. Existing capacity retained.")

        self.save()
        print("Bus updated successfully.")

    def remove_bus(self):
        bus_id = read_id("Enter bus ID: ")
        bus = find_by_id(self.buses, bus_id)
        if not bus:
            print("Bus not found.")
            return
        self.buses.remove(bus)
        self.save()
        print("Bus removed successfully.")
