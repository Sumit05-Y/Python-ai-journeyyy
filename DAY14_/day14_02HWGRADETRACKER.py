students = []

def add_student(name, math, english, science):
    students.append({
        "name": name,
        "math": math,
        "english": english,
        "science": science
    })

def get_average(student):
    return (student["math"] + student["english"] + student["science"]) / 3

def find_top_student():
    return max(students, key=get_average)

add_student("Ram", 85, 90, 80)
add_student("Sita", 95, 92, 88)
add_student("Hari", 70, 75, 78)
add_student("Geeta", 82, 84, 86)

for student in students:
    print(f"{student['name']}: {get_average(student):.2f}")

top = find_top_student()
print(f"\nTop Student: {top['name']} ({get_average(top):.2f})")

high_scorers = {}

for student in students:
    if get_average(student) > 80:
        high_scorers[student["name"]] = get_average(student)

print(high_scorers)

print("\nStudents with average > 80:")
print(high_scorers)