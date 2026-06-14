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
    return (student["math"] + student["english"] + student["science"]) / 3

def find_top_student():
    top = students[0]

    for student in students:
        if get_average(student) > get_average(top):
            top = student

    print("Top Student:", top["name"])
    print("Average:", round(get_average(top), 2))

def view_students():
    for student in students:
        print(student["name"], "-", round(get_average(student), 2))

def high_scorers():
    high = {}

    for student in students:
        avg = get_average(student)
        if avg > 80:
            high[student["name"]] = round(avg, 2)

    print(high)


# some starting data
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