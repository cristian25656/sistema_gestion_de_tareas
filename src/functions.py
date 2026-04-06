def register_new_tasks(id,title,description,priority,state):
    tasks = {
    "id": id,
    "title": title,
    "description": description,
    "priority": priority,
    "state": state
    }
    return tasks
#It records all task data and saves it in a dictionary.
def consult_list_tasks(tasks):
    if not tasks:
        print("There are no registered tasks")
        return
    for task in tasks:
            print(task)
#This function first checks if the searched ID is present; if not, 
#it returns a message and then searches for it using a loop called "task" and prints.
def look_for_task(id,tasks):
    for task in tasks:
        if task ["id"] == id:
            return task
    return None
#Here it searches for an id using the for loop and searching in brackets for the dictionary key in this case the key "id" which returns the searched id.
def update_task(id,tasks):
    task = look_for_task(id,tasks)
    if task:
        print("Leave empty if you don't want to change the value")
        
        new_title = input("New title: ")
        if new_title != "":
            task["title"] = new_title
            
        new_description = input("New description: ")
        if new_description != "":
            task["description"] = new_description
            
        new_priority = input("New priority: ")
        if new_priority != "":
            task["priority"] = new_priority
            
        new_state = input("New state: ")
        if new_state != "":
            task["state"] = new_state
        print("task updated successfully")
        return True
    else:
        print("task not found")
        return False
#Here, the "search" function is first called.
#Then, with this function, searching for the ID, conditionals are created in case you only want to update the title, description, status, etc.
#This returns true if it was changed.
def remove_task(id,tasks):
    tast = look_for_task(id,tasks)
    if tasks:
        tasks.remove(tast)
        return True
    return False
#The function to delete is called search and is deleted with the "remove" function. This returns true if deleted or false otherwise.