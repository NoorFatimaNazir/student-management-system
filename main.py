# Student Management System

students = []


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    grade = calculate_grade(marks)

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks,
        "Grade": grade
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo students found.\n")
        return

    print("\n===== ALL STUDENTS =====")

    for student in students:
        print("----------------------------")
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        print("Marks:", student["Marks"])
        print("Grade:", student["Grade"])


def search_student():
    student_id = input("Enter Student ID to Search: ")

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found")
            print(student)
            return

    print("\nStudent Not Found.\n")


def update_student():
    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["ID"] == student_id:

            print("\nEnter New Information")

            student["Name"] = input("New Name: ")
            student["Age"] = int(input("New Age: "))
            student["Course"] = input("New Course: ")

            marks = float(input("New Marks: "))
            student["Marks"] = marks
            student["Grade"] = calculate_grade(marks)

            print("\nStudent Updated Successfully!\n")
            return

    print("\nStudent Not Found.\n")


def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent Not Found.\n")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You For Using Student Management System!")
        break

    else:
        print("\nInvalid Choice. Please Try Again.")
