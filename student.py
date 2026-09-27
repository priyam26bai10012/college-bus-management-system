from file_manager import load_data, save_data, get_next_id
from validators import required_text, read_id, find_by_id


class StudentManager:
    filename = "students.json"

    def __init__(self):
        self.students = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.students)

    def add_student(self):
        print("\nAdd Student")
        name = required_text("Name: ")
        roll_no = required_text("Roll number: ")
        course = required_text("Course: ")
        year = required_text("Year/Semester: ")

        if any(s["roll_no"].lower() == roll_no.lower() for s in self.students):
            print("A student with this roll number already exists.")
            return

        student = {
            "id": get_next_id(self.students),
            "name": name,
            "roll_no": roll_no,
            "course": course,
            "year": year
        }
        self.students.append(student)
        self.save()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\nID | Name | Roll No | Course | Year")
        print("-" * 60)
        for s in self.students:
            print(f'{s["id"]} | {s["name"]} | {s["roll_no"]} | {s["course"]} | {s["year"]}')

    def search_student(self):
        term = required_text("Enter name or roll number: ").lower()
        results = [
            s for s in self.students
            if term in s["name"].lower() or term in s["roll_no"].lower()
        ]
        if not results:
            print("No matching student found.")
            return
        for s in results:
            print(f'ID: {s["id"]}, Name: {s["name"]}, Roll: {s["roll_no"]}, '
                  f'Course: {s["course"]}, Year: {s["year"]}')

    def update_student(self):
        student_id = read_id("Enter student ID: ")
        student = find_by_id(self.students, student_id)
        if not student:
            print("Student not found.")
            return

        print("Press Enter to keep the existing value.")
        name = input(f'Name [{student["name"]}]: ').strip()
        course = input(f'Course [{student["course"]}]: ').strip()
        year = input(f'Year [{student["year"]}]: ').strip()

        if name:
            student["name"] = name
        if course:
            student["course"] = course
        if year:
            student["year"] = year

        self.save()
        print("Student updated successfully.")

    def remove_student(self):
        student_id = read_id("Enter student ID: ")
        student = find_by_id(self.students, student_id)
        if not student:
            print("Student not found.")
            return
        self.students.remove(student)
        self.save()
        print("Student removed successfully.")
