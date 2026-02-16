import datetime
import json

# Variables 
studentsRemoved = 0
# Function for displaying the menu

def showMenu():
    print("""\n ---- Student Management System ---- 
1. Add Student
2. Search For A Student Info
3. Update A Particular Student Info
4. Delete A Particular Student Info Or The Whole Database
5. Show Statistics
6. Save & Exit
--------------------------------------------------
""")


# Function for adding a student info

def addStudent(students) :
    
    rollNo = int(input("Enter the roll number of the student : "))
    if rollNo in students:
        print("❎ | Roll No Already Exists!")
        return
    
    name = input("Enter the name of the student: ")
    gender = input("Enter the gender : ")
    age = int(input("Enter the age : "))
    address = input("Enter the address of the student : ")
    marks = float(input("Enter the marks scored by the student : "))
    timeStamp = datetime.datetime.now()


    students[rollNo] = {
        "rollNo" : rollNo,
        "name" : name,
        "gender" : gender,
        "age" : age,
        "address" : address,
        "marks" : marks,
        "timeStamp" : timeStamp.strftime("%c")
    }

    print("✅ | Student Info added successfully!")


# Funnction for searching for a particular student information

def searchForStudent(students):
    if not students:
        print("❎ | No records found. Try addding information and retry!")
    else :
        choice = int(input("Options Available\n1. Search By Roll Number\n2. Search by Name [ Case Sensitive ]\nEnter Your Choice : "))
        if choice == 1:
            rollNo = int(input("Enter the roll no : "))
        elif choice == 2:
            name = input("Enter the name of the student : ")
        else :
            print("❎ | Invalid Choice. Reverting back to the previous menu!")
            return
        if choice == 1 :
            if rollNo in students:
                print("✅ | Student Info Found!")
                print(rollNo, "|", students[rollNo]["name"], "|", students[rollNo]["gender"], "|", students[rollNo]["age"], "|", students[rollNo]["address"], "|", students[rollNo]["marks"] )
            else:
                print("❎ | Student Info Not Found")
                return
        elif choice == 2 :
            found = False
            for rollNo, data in students.items():
                if data["name"] == name:
                    print("✅ | Student Info Found!")
                    print(rollNo, "|", students[rollNo]["name"], "|", students[rollNo]["gender"], "|", students[rollNo]["age"], "|", students[rollNo]["address"], "|", students[rollNo]["marks"] )
                    found = True
                    break
            if not found:
                print("❎ | Student Info Not Found")
    



#Function to update a particular student info

def updateStudent(students):
    rollNo = int(input("Enter the roll no. of the student that has to be updated : "))
    if rollNo not in students:
        print("❎ | Roll No Does Not Exist. Falling back to the previous menu!")
        return
    else:
        choice = int(input("Options Avaiable\n1. Change Name\n2. Change Gender\n3. Change Age\n4. Change Address\n5. Change Marks\nEnter Your Choice : "))
        match choice:
            case 1:
                name = input("Enter the name : ")
                students[rollNo]["name"] = name
                print("✅ | Student's Name Updated Successfully!")
            case 2:
                gender = input("Enter the gender : ")
                students[rollNo]["gender"] = gender
                print("✅ | Student's Gender Updated Successfully!")
            case 3:
                age = int(input("Enter the age : "))
                students[rollNo]["age"] = age
                print("✅ | Student's Age Updated Successfully!")
            case 4:
                address = input("Enter the address : ")
                students[rollNo]["address"] = address
                print("✅ | Student's Address Updated Successfully!")
            case 5:
                marks = float(input("Enter the marks : "))
                students[rollNo]["marks"] = marks
                print("✅ | Student's Marks Updated Successfully!")
            case _:
                print("❎ | Invalid Choice. Reverting back to the previous menu!")
                return


# Function to remove a particular student's info and to clear the student info database

def removeStudent(students):
    global studentsRemoved
    choice = int(input("Options Available :\n1. Delete A Particular Student Info\n2. Delete The Whole Database\n--------------------------------\nYour Choice : "))
    # To clear the information of a particular student
    if choice == 1:
        rollNo = int(input("Enter the roll number to be deleted : "))
        if rollNo not in students:
            print("❎ | Roll No Does Not Exist. Falling back to the previous menu!")
            return
        del students[rollNo]
        print("✅ | Student's Info Deleted Successfully!")
        studentsRemoved += 1
    # To clear the student info database
    elif choice == 2:
        secChoice = (input("Are you sure you want to delete the whole database? Reply with [y/n] : "))
        if secChoice == 'Y' or secChoice == 'y' :
            studentsRemoved += len(students)
            students.clear()
        elif secChoice == 'n' or secChoice == 'n':
            print("❎ | Operation Cancelled. Reverting back to the previous menu!")
            return


# Function To Show Statistics

def showStatistics(students):
    if not students:
        print("❎ | No records available for statistics")
        return

    totalMarks = 0
    minMarks = 101.0
    maxMarks = -1.0
    minMarksScoredBy = None
    maxMarksScoredBy = None

    for data in students.values():
        marks = data["marks"]
        totalMarks += marks

        if marks > maxMarks:
            maxMarks = marks
            maxMarksScoredBy = data["name"]
        if marks < minMarks:
            minMarks = marks
            minMarksScoredBy = data["name"]

    totalStudents = len(students)
    avgMarks = totalMarks / totalStudents

    print(f"""----- Class Statistics -----

Maximum Marks            : {maxMarks}
Maximum Marks Scored By  : {maxMarksScoredBy}
Minimum Marks            : {minMarks}
Minimum Marks Scored By  : {minMarksScoredBy}
Class Average Marks      : {avgMarks:.2f}

----- System Statistics -----
Total Students           : {totalStudents}
Total Students Removed   : {studentsRemoved}
""")
    
# Saving the information in JSON Format

def saveToFile(students, filename="studentInfo.json"):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)
    print("✅ | Data saved successfully!")

# Loading the information from the JSON File

def loadFromFile(filename="students.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return {int(k): v for k, v in data.items()}
    except FileNotFoundError:
        return {}





    


