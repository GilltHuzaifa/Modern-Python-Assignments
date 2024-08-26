def manage_student_database():

    students = []
    id_counter = 1
    while True:

        name = input("Please enter the student's name (or type 'stop' to finish): ")
        if name.lower() == "stop":
            print("Goodbye! 😄")
            break

        if any(student[1] == name for student in students):
            print("This name is already in the list.")
            continue

        students.append((id_counter, name))
        id_counter += 1

        print("Complete List of Students (Tuples):")
        for student in students:
            print(tuple(student))
        
        print("\nList of Students with IDs:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}")
        
        print("\nTotal number of students:", len(students))

        print("Total length of all student names combined:", sum(len(student[1]) for student in students))

        longest_name = max(students, key=lambda x: len(x[1]))

        shortest_name = min(students, key=lambda x: len(x[1]))

        print(f"The student with the longest name is: {longest_name[1]}")

        print(f"The student with the shortest name is: {shortest_name[1]}")



manage_student_database()


        