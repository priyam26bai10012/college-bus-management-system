from datetime import date
from file_manager import load_data, save_data
from validators import read_id, find_by_id


class AttendanceManager:
    filename = "attendance.json"

    def __init__(self, student_manager):
        self.student_manager = student_manager
        self.records = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.records)

    def mark_attendance(self):
        student_id = read_id("Student ID: ")
        student = find_by_id(self.student_manager.students, student_id)
        if not student:
            print("Student not found.")
            return

        today = date.today().isoformat()
        status = input("Present or Absent (P/A): ").strip().upper()

        if status not in ("P", "A"):
            print("Invalid status.")
            return

        existing = next(
            (r for r in self.records
             if r["student_id"] == student_id and r["date"] == today),
            None
        )

        if existing:
            existing["status"] = status
            print("Today's attendance updated.")
        else:
            self.records.append({
                "student_id": student_id,
                "date": today,
                "status": status
            })
            print("Attendance marked.")

        self.save()

    def get_student_summary(self, student_id):
        records = [r for r in self.records if r["student_id"] == student_id]
        present = sum(1 for r in records if r["status"] == "P")
        absent = sum(1 for r in records if r["status"] == "A")
        total = len(records)
        percentage = (present / total * 100) if total else 0
        return present, absent, percentage

    def view_attendance(self):
        student_id = read_id("Student ID: ")
        student = find_by_id(self.student_manager.students, student_id)
        if not student:
            print("Student not found.")
            return

        records = [r for r in self.records if r["student_id"] == student_id]
        if not records:
            print("No attendance records found.")
            return

        print(f'\nAttendance for {student["name"]}')
        for r in records:
            print(f'{r["date"]}: {"Present" if r["status"] == "P" else "Absent"}')

        present, absent, percentage = self.get_student_summary(student_id)
        print(f"Present: {present}, Absent: {absent}, Attendance: {percentage:.1f}%")
