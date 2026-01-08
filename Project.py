import json

def load_tasks():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

tasks=load_tasks()

def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file)


def add_task(tasks):
    task= input("Enter a task name: ")
    task1=task.strip()
    if task1=="":
        print("Enter valid task")
    else:
        tasks.append({"title":task1, "done":False})
        print("TASK ADDED.")
        save_tasks(tasks)


def view_tasks(tasks):
    count=0
    if not tasks:
        print("No tasks exist yet.")
    
    else:
        print("\n Your Tasks:")
        for i,task in enumerate(tasks, start=1):
            if task["done"]:
                 status ="✓"
                 count+=1 
                 print(f"{i}. [{status}] {task['title']}")
            else:
                status="✗"
                print(f"{i}. [{status}] {task['title']}")
    print(f"Total number of tasks: {i}")
    print(f"Total tasks done :{count}")


def edit_tasks(tasks):
    view_tasks(tasks)
    try:
        task_no =int(input("Enter task number to update title:"))
        if 1 <= task_no <=len(tasks):
            old_title=tasks[task_no-1]
            new_title=input('Enter the new title:')
            old_title['title']= new_title
            save_tasks(tasks)
        
        else:
            print("Enter a valid choice:")

    except ValueError:
        print('Enter a number please:')
    

def task_mark(tasks):
    if not tasks:
        print("no tasks to mark.")
        
    else:
        try:
            task_no =int(input("Enter task number to mark done:"))
            if 1 <= task_no <=len(tasks):
                tasks[task_no-1]["done"] = True
                print("Task marked as done.")
            else:
                print('Enter a valid choice:')
            
        except ValueError:
            print('Enter a number please:')
          
    save_tasks(tasks)

def search_tasks(tasks):
    key_word=input('Enter a keyword:')
    word= key_word.lower()
    for i,task in enumerate(tasks,start=1):
        if word in task['title'].lower():
            print(f"Results found: {i}, {task['title']}")


def delete_tasks(tasks):
    if not tasks:
            print("No tasks to delete.")
    else:
        task_no= int(input("Enter the task number to delete:"))

        if 1 <=task_no <=len(tasks):
            choice=input(f"Are you sure you want to delete task- {tasks[task_no - 1]['title']}-(yes/no):")

            if "y" in choice.lower():
                deleted_task=tasks.pop(task_no-1)
                print(f" Deleted task: {deleted_task['title']}")

            elif 'n' in choice.lower():
                print("Task not deleted.")
            else:
                print("Please enter a valid choice.")
        
        else:
            print("Invalid task number.")
    save_tasks(tasks)

def exit_tasks(tasks):
     print("Exited sucessfully..")
     

while True:
    print("\n--- TO DO LIST---")
    print("1.Add a Task")
    print("2.View Tasks")
    print("3.Edit Task Title")
    print("4.Mark Task as done")
    print("5.Search Tasks")
    print("6.Delete Tasks'")
    print("7.Exit")



    choice= input("Enter a choice:")

    if choice =="1":
        add_task(tasks)

    elif choice =="2":
        view_tasks(tasks)

    elif choice=='3':
        edit_tasks(tasks)

    elif choice =="4":
        task_mark(tasks)
    
    elif choice=="5":
        search_tasks(tasks)

    elif choice =="6":
        delete_tasks(tasks)

    elif choice =="7":
        exit_tasks(tasks)
        break

    else:
        print("Invalid task number.")