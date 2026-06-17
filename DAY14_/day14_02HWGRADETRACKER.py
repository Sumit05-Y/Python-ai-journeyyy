students = []


def add_student(name, math, english, science):
    student = {
        "name": name,
        "math": math,
        "english": english,
        "science": science
    }
    students.append(student)
    print("Student added!")


def get_average(student):
    marks_avg = (
        student["math"] +
        student["english"] +
        student["science"]
    ) / 3

    with open("grade.txt", "a") as f:
        f.write("-----Average marks------\n")
        f.write(f"{student['name']} : {marks_avg:.2f}\n")

    return marks_avg


def find_top_student():
    with open("grade.txt", "a") as f:
        student1 = []

        for student in students:
            student1.append(get_average(student))

        top_marks = max(student1)
        index_pointer = student1.index(top_marks)

        print(students[index_pointer])
        print(top_marks)

        f.write("----Top student-----\n")
        f.write(f"{students[index_pointer]}\n")
        f.write(f"{top_marks}\n")


def view_students():
    print(f'{"NAME":<15}{"ENGLISH":<10}{"MATHS":<10}{"SCIENCE":<10}{"AVERAGE":<10}')

    for student in students:
        print(
            f'{student["name"]:<15}'
            f'{student["english"]:<10}'
            f'{student["math"]:<10}'
            f'{student["science"]:<10}'
            f'{get_average(student):<10.2f}'
        )


def high_scorers():
    with open("grade.txt", "a") as f:
        high = {}

        for student in students:
            avg = get_average(student)
            if avg > 80:
                high[student["name"]] = round(avg, 2)

        print(high)

        f.write("----High score-----\n")
        f.write(f"{high}\n")


add_student("Ram", 85, 90, 80)
add_student("Sita", 95, 92, 88)
add_student("Hari", 70, 75, 78)
add_student("Geeta", 82, 84, 86)


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Find Top Student")
    print("4. Show High Scorers")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        math = float(input("Enter math marks: "))
        english = float(input("Enter english marks: "))
        science = float(input("Enter science marks: "))

        add_student(name, math, english, science)

    elif choice == "2":
        view_students()

    elif choice == "3":
        find_top_student()

    elif choice == "4":
        high_scorers()

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice")