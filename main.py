import time
print("\n","-"*10,"📝 Welcome To-Do List App","-"*10)
task=[ ]
def display():
    for i in range(len(task)):
        print(f"{i+1}. {task[i]}")
def Home():
    main_list=input("\nclick enter to continue: ".title())
while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit\n")
    try:
        choice=int(input("Enter your choice (1-4): "))
        # add_task
        if choice==1:
            add=input("Enter your task: ")
            if not add:
                print("❌ No Task added")
            else:
                task.append(add)
                print("✅ Task added!")
                Home()
        # view_task
        elif choice==2:
            if not task:
                print("🤷 there is no tasks".title())
            else:
                print("📋 your tasks:".title())
                display()
                Home()
        # delete_task
        elif choice==3:
            if not task:
                print("🤷 there is no tasks".title())
            else:
                print("\n📋 your tasks:".title())
                display()
                try:
                    delete = int(input("Choose number to delete: "))
                    if delete < 1 or delete > len(task):
                        print("Invalid choice! Try again".title())
                    else:
                        removed_task = task.pop(delete - 1)
                        print(f"🗑️  Task deleted: {removed_task}")         
                except ValueError:
                    print("Invalid choice! Please enter a valid number.".title())
                Home()
        # exit
        elif choice==4:
            print("👋 goodbye!".title())
            time.sleep(1.5)
            break

        # invalid
        else:
            print("invalid choice! try again".title())
            Home()

    except ValueError:
       print("Invalid choice! Please enter a valid number.".title())
       Home()




