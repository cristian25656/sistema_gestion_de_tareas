from ui.menus import*
from src.functions import *

welcome()
repository_tasks = []
star = 1
#The list is created and a variable called "star" is created to open and control the "while" loop
while star != 0:
    try:
        menu()
        option = int(input("Choose the option you want: "))        
        if option == 1:
            id = int(input("Enter the ID: "))
            title = str(input("Enter the title: "))
            description = str(input("Enter the description: "))
            priority = str(input("Enter the priority: "))
            state = str(input("Enter the state: "))
            tasks = register_new_tasks(id,title,description,priority,state)
            repository_tasks.append(tasks)
#It is added to the repository using the append function, and all the variables to be used are requested. The add function is then called.
        elif option == 2:
            consult_list_tasks(repository_tasks)
#The function to display the list is called
        elif option == 3:
            look_up_task = int(input("Enter the task ID: "))
            task = look_for_task(look_up_task,repository_tasks)
            if task:
                print("task found: ", task)
            else:
                print("task not found")
#The function is called and the search results are displayed on the screen, and also if nothing is found.
        elif option == 4:
            id_update = int(input("Enter the task ID:  "))
            update_task(id_update,repository_tasks)
#The ID is requested and the update function is called
        elif option == 5:
            id_remove = int(input("Enter the ID of the task to delete: "))
            confirm = input(f"""
Are you sure you want to delete: {id_remove}? 
Enter: (yes/no): 
""")
            if confirm == "yes":
                if remove_task(id_remove,repository_tasks):
                    print("Your task has been deleted")
                else:
                    print("Your task to remove was not found.")
            elif confirm == "no":
                print("task not removed")
            else:
                print("Error,enter a valid value")
#The ID is requested and a variable is created to confirm whether that ID should be deleted, and then a condition is applied to see if what is to be deleted was found.
        elif option == 6:
            print("good bye, see you soon")
            star = 0
        else:
            print("Error,enter a valid value")  
    except ValueError:
        print("Error,enter a valid value")
#I use try/except so that the program stops abruptly if there is a syntax error