tasks = []

def addTask():
    task = input("please enter a task :")
    tasks.append(task)
    print(f"Task' {task}' added to the list.")
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("current Tasks")
        for index, task in enumerate(tasks):
            print(f"Task#{index}. {task}")
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been removed.")
        else:
            print(f"Task #{tasktoDelete} was not found.")
    except:
        print("Invalid input")



if __name__ == "__main__":
    ## Creating a loop to run the app
    print("Welcome to the to do List App ._.")
while True:
    print("/n")
    print("Please select one of the following options")
    print("___________________________________________")
    print("1. Add a task")
    print("2. Delete a Task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif (choice == "3"):
        listTasks()
    elif (choice == "4"):
        break
    else:
        print("Invalid input. Try again :)")

print("Good bye :)")

