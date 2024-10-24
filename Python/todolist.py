def to_do_list():
    # store the to do list in a list
    incomplete_tasks = []
    completed_tasks = []

    # introduction
    print("Things I can do! No Special Software NEEDED.")

    #get user first task
    first_task = input("Enter your first task: ")
    incomplete_tasks.append(first_task)

    #ask if it wants to add another
    #if yes ask again for a new task
    #if not proceed to ask if wants to mark a task as completed
    while True:
        print("Choose an option!")
        print("[1] Enter a new task")
        #print("[2] Mark a task as completed")
        print("[2] Exit")

        user_choice = int(input("Make a choice: "))
        if user_choice == 1:
            new_task = input("Enter a new task: ")
            incomplete_tasks.append(new_task)
        elif user_choice == 2:
            print("Your To-Do List:")
            print(incomplete_tasks)
            print("Choose the task you wish to mark completed. Choose the number of the task with the first task being number 0.")
            task_completed = int(input("Choose: "))
            if task_completed =
        elif user_choice == 2:
            print(completed_tasks)
            "Thanks for using our To-DO List!"
            return

    #if user doesn't want to make any further change, ask if want to save it for later


    # if not break the code
    

to_do_list()