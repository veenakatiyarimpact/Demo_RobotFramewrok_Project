import pickle

def store_student_records():
    f = open("student.dat", "wb")

    n = int(input("Enter number of students: "))

    for i in range(n):
        rollno = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        student = [rollno, name]
        pickle.dump(student, f)

    f.close()

    print("Student records stored successfully!")


def searchRollno(rollNo):

    f = open("student.dat", "rb")
    rollNo = int(rollNo)

    found = False

    try:
        while True:
            student = pickle.load(f)
            studentRollNo = student[0]
            studentName = student[1]

            if studentRollNo == rollNo:
                print("Roll Number:", studentRollNo)
                print("Student Name:", studentName)
                found = True
                break

    except EOFError:
        pass

    if found == False:
        print("Error: Roll Number not found!")

    f.close()


store_student_records()
searchRollno(10)