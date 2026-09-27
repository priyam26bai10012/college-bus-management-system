from validators import read_id, find_by_id


class ReportManager:
    def __init__(self, student_manager, bus_manager, route_manager,
                 allocation_manager, attendance_manager):
        self.students = student_manager
        self.buses = bus_manager
        self.routes = route_manager
        self.allocations = allocation_manager
        self.attendance = attendance_manager

    def student_bus_details(self):
        student_id = read_id("Student ID: ")
        student = find_by_id(self.students.students, student_id)
        if not student:
            print("Student not found.")
            return

        allocation = self.allocations.assigned_student(student_id)
        print(f'\nStudent: {student["name"]}')
        print(f'Roll No: {student["roll_no"]}')

        if not allocation:
            print("Bus allocation: Not assigned")
            return

        bus = find_by_id(self.buses.buses, allocation["bus_id"])
        route = find_by_id(self.routes.routes, allocation["route_id"])
        print(f'Bus: {bus["number"] if bus else "Unknown"}')
        print(f'Route: {route["name"] if route else "Unknown"}')

    def route_students(self):
        route_id = read_id("Route ID: ")
        route = find_by_id(self.routes.routes, route_id)
        if not route:
            print("Route not found.")
            return

        print(f'\nStudents on route: {route["name"]}')
        count = 0
        for allocation in self.allocations.allocations:
            if allocation["route_id"] == route_id:
                student = find_by_id(self.students.students, allocation["student_id"])
                if student:
                    print(f'- {student["name"]} ({student["roll_no"]})')
                    count += 1
        print(f"Total students: {count}")

    def bus_occupancy(self):
        print("\n--- BUS OCCUPANCY ---")
        for bus in self.buses.buses:
            occupied = self.allocations.bus_occupancy_count(bus["id"])
            available = max(bus["capacity"] - occupied, 0)
            print(
                f'Bus {bus["number"]}: '
                f'{occupied}/{bus["capacity"]} occupied, '
                f'{available} seats available'
            )

    def attendance_summary(self):
        print("\n--- ATTENDANCE SUMMARY ---")
        if not self.students.students:
            print("No students found.")
            return

        for student in self.students.students:
            present, absent, percentage = self.attendance.get_student_summary(student["id"])
            print(
                f'{student["name"]} ({student["roll_no"]}) - '
                f'Present: {present}, Absent: {absent}, '
                f'Attendance: {percentage:.1f}%'
            )
