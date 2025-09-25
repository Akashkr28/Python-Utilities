def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to finish: ").strip()
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists. Please enter a different name.")
            continue

        try:
            marks =float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks.")
    
    return students

def display_report(students):
    if not students:
        print("No student data to display.")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score]
    bottomer = [name for name, score in students.items() if score == min_score]

    print("\nStudent Report: ")
    print("-" * 30)
    print(f"Total Students: {len(students)}")
    print(f"Average Marks for students: {average:.2f}")
    print(f"Highest Marks: {max_score} by {', '.join(topper)}")
    print(f"Lowest Marks: {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks: ")
    for name, score in students.items():
        print(f" - {name}: {score}")

students = collect_student_data()
display_report(students)