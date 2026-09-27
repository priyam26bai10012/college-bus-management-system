from file_manager import load_data, save_data, get_next_id
from validators import read_id, find_by_id


class AllocationManager:
    filename = "allocations.json"

    def __init__(self, student_manager, bus_manager, route_manager):
        self.student_manager = student_manager
        self.bus_manager = bus_manager
        self.route_manager = route_manager
        self.allocations = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.allocations)

    def assigned_student(self, student_id):
        return next(
            (a for a in self.allocations if a["student_id"] == student_id),
            None
        )

    def bus_occupancy_count(self, bus_id):
        return sum(1 for a in self.allocations if a["bus_id"] == bus_id)

    def assign_student(self):
        student_id = read_id("Student ID: ")
        if not find_by_id(self.student_manager.students, student_id):
            print("Student not found.")
            return
        if self.assigned_student(student_id):
            print("Student is already assigned to a bus.")
            return

        bus_id = read_id("Bus ID: ")
        bus = find_by_id(self.bus_manager.buses, bus_id)
        if not bus:
            print("Bus not found.")
            return

        if self.bus_occupancy_count(bus_id) >= bus["capacity"]:
            print("This bus is full.")
            return

        route_id = read_id("Route ID: ")
        if not find_by_id(self.route_manager.routes, route_id):
            print("Route not found.")
            return

        allocation = {
            "id": get_next_id(self.allocations),
            "student_id": student_id,
            "bus_id": bus_id,
            "route_id": route_id
        }
        self.allocations.append(allocation)
        self.save()
        print("Student assigned successfully.")

    def view_allocations(self):
        if not self.allocations:
            print("No allocations found.")
            return
        for a in self.allocations:
            student = find_by_id(self.student_manager.students, a["student_id"])
            bus = find_by_id(self.bus_manager.buses, a["bus_id"])
            route = find_by_id(self.route_manager.routes, a["route_id"])
            print(
                f'Allocation {a["id"]}: '
                f'{student["name"] if student else "Unknown student"} | '
                f'Bus {bus["number"] if bus else "Unknown"} | '
                f'Route {route["name"] if route else "Unknown"}'
            )

    def change_allocation(self):
        student_id = read_id("Student ID: ")
        allocation = self.assigned_student(student_id)
        if not allocation:
            print("No allocation found for this student.")
            return

        bus_id = read_id("New bus ID: ")
        bus = find_by_id(self.bus_manager.buses, bus_id)
        if not bus:
            print("Bus not found.")
            return
        if self.bus_occupancy_count(bus_id) >= bus["capacity"] and allocation["bus_id"] != bus_id:
            print("This bus is full.")
            return

        route_id = read_id("New route ID: ")
        if not find_by_id(self.route_manager.routes, route_id):
            print("Route not found.")
            return

        allocation["bus_id"] = bus_id
        allocation["route_id"] = route_id
        self.save()
        print("Allocation changed successfully.")

    def remove_allocation(self):
        student_id = read_id("Student ID: ")
        allocation = self.assigned_student(student_id)
        if not allocation:
            print("No allocation found.")
            return
        self.allocations.remove(allocation)
        self.save()
        print("Allocation removed successfully.")
