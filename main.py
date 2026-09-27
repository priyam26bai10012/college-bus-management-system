from student import StudentManager
from bus import BusManager
from route import RouteManager
from allocation import AllocationManager
from attendance import AttendanceManager
from reports import ReportManager


def pause():
    input("\nPress Enter to continue...")


def student_menu(student_manager):
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Remove student")
        print("6. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            student_manager.add_student()
        elif choice == "2":
            student_manager.view_students()
        elif choice == "3":
            student_manager.search_student()
        elif choice == "4":
            student_manager.update_student()
        elif choice == "5":
            student_manager.remove_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
        if choice != "6":
            pause()


def bus_menu(bus_manager):
    while True:
        print("\n--- BUS MANAGEMENT ---")
        print("1. Add bus")
        print("2. View buses")
        print("3. Update bus")
        print("4. Remove bus")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            bus_manager.add_bus()
        elif choice == "2":
            bus_manager.view_buses()
        elif choice == "3":
            bus_manager.update_bus()
        elif choice == "4":
            bus_manager.remove_bus()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        if choice != "5":
            pause()


def route_menu(route_manager):
    while True:
        print("\n--- ROUTE MANAGEMENT ---")
        print("1. Add route")
        print("2. View routes")
        print("3. Update route")
        print("4. Remove route")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            route_manager.add_route()
        elif choice == "2":
            route_manager.view_routes()
        elif choice == "3":
            route_manager.update_route()
        elif choice == "4":
            route_manager.remove_route()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        if choice != "5":
            pause()


def allocation_menu(allocation_manager):
    while True:
        print("\n--- BUS ALLOCATION ---")
        print("1. Assign student to bus")
        print("2. View allocations")
        print("3. Change allocation")
        print("4. Remove allocation")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            allocation_manager.assign_student()
        elif choice == "2":
            allocation_manager.view_allocations()
        elif choice == "3":
            allocation_manager.change_allocation()
        elif choice == "4":
            allocation_manager.remove_allocation()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        if choice != "5":
            pause()


def attendance_menu(attendance_manager):
    while True:
        print("\n--- ATTENDANCE ---")
        print("1. Mark attendance")
        print("2. View student attendance")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            attendance_manager.mark_attendance()
        elif choice == "2":
            attendance_manager.view_attendance()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
        if choice != "3":
            pause()


def report_menu(report_manager):
    while True:
        print("\n--- REPORTS ---")
        print("1. Student bus details")
        print("2. Route-wise students")
        print("3. Bus occupancy")
        print("4. Attendance summary")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            report_manager.student_bus_details()
        elif choice == "2":
            report_manager.route_students()
        elif choice == "3":
            report_manager.bus_occupancy()
        elif choice == "4":
            report_manager.attendance_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        if choice != "5":
            pause()


def main():
    student_manager = StudentManager()
    bus_manager = BusManager()
    route_manager = RouteManager()
    allocation_manager = AllocationManager(student_manager, bus_manager, route_manager)
    attendance_manager = AttendanceManager(student_manager)
    report_manager = ReportManager(
        student_manager, bus_manager, route_manager,
        allocation_manager, attendance_manager
    )

    while True:
        print("\n" + "=" * 50)
        print("       COLLEGE BUS MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Student Management")
        print("2. Bus Management")
        print("3. Route Management")
        print("4. Bus Allocation")
        print("5. Attendance")
        print("6. Reports")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_menu(student_manager)
        elif choice == "2":
            bus_menu(bus_manager)
        elif choice == "3":
            route_menu(route_manager)
        elif choice == "4":
            allocation_menu(allocation_manager)
        elif choice == "5":
            attendance_menu(attendance_manager)
        elif choice == "6":
            report_menu(report_manager)
        elif choice == "7":
            print("Thank you for using the College Bus Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
