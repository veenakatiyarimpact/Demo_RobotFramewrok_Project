
import pickle

def store_student_records():
    f = open("student1.dat", "wb")

    n = int(input("Enter number of students: "))

    for i in range(n):
        rollno = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Student Marks: "))

        student = [rollno, name, marks]
        pickle.dump(student, f)

    f.close()

    print("Student records stored successfully!")


def updateMarks(rollNo):

    f = open("student1.dat", "rb")

    records = []
    found = False

    try:
        while True:
            student = pickle.load(f)

            if student[0] == rollNo:
                print("Roll Number:", student[0])
                print("Student Name:", student[1])
                print("Old Marks:", student[2])

                marks = float(input("Enter Students new marks: "))
                student[2] = marks

                found = True

            records.append(student)

    except EOFError:
        pass

    f.close()

    if found:
        f = open("student1.dat", "wb")

        for student in records:
            pickle.dump(student, f)

        f.close()

        print("Marks updated successfully!")

    else:
        print("Error: Roll Number not found!")


store_student_records()
updateMarks(10)
