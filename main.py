import os
from student import *
from search_student import *
from add_student import add_student
from print_allstud import printAllStudents

def main_menu():
    while True:
        log = input("Please enter your ID Number: ")
        try:
            with open("studentlist.txt", "r") as f:
                students = f.readlines()
                ids = [line.split(",")[2] for line in students]  # Extract ID numbers

            if log in ids:
                logged_in_user = None
                for line in students:
                    details = line.strip().split(",")
                    if details[2] == log:
                        logged_in_user = details
                        break
                
                print(f"Welcome, {logged_in_user[0]}!")
            else:
                print("Invalid ID Number!")
                continue
        except FileNotFoundError:
            print("No student data found. Please register a new student first.")
            continue

        print("Please choose from the following options:")
        print("1. Check your own information")
        print("2. Search for other student's information")
        print("3. Add a new student")
        print("4. Print all students in the list")
        print("5. Exit")
        choice = input("Your choice: ")

        os.system("cls")

        if choice == "1":
            if logged_in_user:
                print(f"=== Your Information ===")
                print(f"Name: {logged_in_user[0]}")
                print(f"Age: {logged_in_user[1]}")
                print(f"ID: {logged_in_user[2]}")
                print(f"Email: {logged_in_user[3]}")
                print(f"Phone: {logged_in_user[4]}")
                print("========================")
            else:
                print("Could not find your information. Please log in again.")
        
        elif choice == "2":
            search_id = input("Enter the ID number of the student you want to search: ")
            try:
                with open("studentlist.txt", "r") as f:
                    students = f.readlines()
                    found = False
                    for line in students:
                        details = line.strip().split(",")
                        if details[2] == search_id:
                            print(f"=== Student Information ===")
                            print(f"Name: {details[0]}")
                            print(f"Age: {details[1]}")
                            print(f"ID: {details[2]}")
                            print(f"Email: {details[3]}")
                            print(f"Phone: {details[4]}")
                            print("===========================")
                            found = True
                            break
                    if not found:
                        print("Student not found.")
            except FileNotFoundError:
                print("No student data found.")
        
        elif choice == "3":
            while True:
                print("=== Add New Student ===")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                idnum = input("Enter Student ID: ")
                email = input("Enter Email Address: ")
                phone = input("Enter Phone Number: ")

                add_student(None, name, age, idnum, email, phone)
                print(f"Student {name} added successfully!")

                another = input("Do you want to add another student? (Y/N): ").upper()
                if another == "N":
                    print("Returning to main menu.")
                    break
        
        elif choice == "4":
            printAllStudents()

        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
