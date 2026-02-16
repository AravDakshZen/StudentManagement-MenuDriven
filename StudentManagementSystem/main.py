# File Importing
from services import showMenu, addStudent, searchForStudent,  updateStudent, removeStudent, showStatistics, saveToFile, loadFromFile
# Variables
students = {

}

# Main function
def main():
    endMenu = True
    students = loadFromFile() 
    while endMenu:
        showMenu()
        choice = int(input("Enter your choice : "))
        match choice:
            case 1:
                addStudent(students)
            case 2:
                searchForStudent(students)
            case 3:
                updateStudent(students)
            case 4:
                removeStudent(students)
            case 5:
                showStatistics(students)
            case 6:
                saveToFile(students)
                print("Saved the information and exited properly!")
                endMenu = False
            case _:
                print("The choice is inavlid. Please retry!")

if __name__ == "__main__":
    main()

