
import csv

# Writing data into CSV file
with open('./././TestData/Excel_Data/userData.csv', 'w', newline='') as file:

    writer1 = csv.writer(file)

    writer1.writerow(['userid', 'password'])

    while True:
        userid = input("Enter User ID (or 'exit' to quit): ")

        if userid.lower() == 'exit':
            break

        password = input("Enter Password: ")

        writer1.writerow([userid, password])


print("Data written successfully!")

# Reading data from CSV file
with open('./././TestData/Excel_Data/userData.csv', 'r', newline='') as file1:

    reader1 = csv.reader(file1)
    userid = input("Enter User ID to search: ")

    for row in reader1:
        print(row)
        if row[0] == userid:
            print("Password : ", row[1])
