#press 1 to add task
#press 2 to delete task (focus on this last)
    #when deleting show user all tasks
        #1. task - priority
        #2. task - priority
#press q to quit
#tasks add in dictionary{title:priority} priority = high medium low
#each dictionary needs to be in an array
#array will represent list of tasks


tasks = []
#empty array

print("Welcome to Task Manager!")
#no need to have this appear every time in start_menu

def view_all_tasks():
    for info in tasks:
        i = tasks.index(info) + 1
        print(f"{i} - {info['Title']} - {info['Priority']}")
#function to view data <TASK> from dictionary <TASKS>

def start_menu():
#    print("Welcome to Task Manager!")
    print("Press 1 to Enter New Task.")
    print("Press 2 to Delete Old Task.")
    print("Press 3 to View All Tasks.")
    print("Press q to Quit.")
#menu will display each time it is called upon, but has NO INPUT FUNCTION, just text

user_input = ""
#gives no value to user_input by default

def add_task():
    print("Enter Task and Priority (High/Medium/Low): ")
    #tell them what to enter and pre-defined values for priority
    task_name = input("Task Name: ")
    task_priority = input("Priority: ")
    task = {"Title": task_name, "Priority": task_priority}
    #storing input into a dictionary <task>; <task> is ONLY in this function
    tasks.append(task)
    #add input key and value to tasks array


def delete_task():

    print("Which task would you like to delete? ")
    view_all_tasks()
    key = int(input("Enter task you want to delete. "))
    for key in tasks: #checking if entry is in dictionary
        tasks.remove(key)
    return tasks


while user_input != "q":
    start_menu()
    #while user does not hit q run start_menu function
    user_input = input("Enter Choice Now: ").lower()
    if user_input == "1":
        add_task()
    if user_input == "2":
        delete_task()
    if user_input == "3":
        view_all_tasks()
    else:
        print("Goodbye.")
