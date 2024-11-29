import tkinter as tk

# List will hold all the tasks
tasks =[]

#Add tasks to the tasks list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)   #add task to the listbox
        task_entry.delete(0, tk.END) # clear the input field
        print(f"Task '{task}' added!")


# Display all the tasks
def view_tasks():
    task_listbox.delete(0,tk.END)   # clear current listbox items
    if tasks:
        for task in tasks:
            task_listbox.insert(tk.END, task)

    else:
        task_listbox.insert(tk.END, "No tasks yet!")

# Remove a task
def remove_task():
    selected_task_index = task_listbox.curselection()  # get the selected task index
    if selected_task_index:
        removed = tasks.pop(selected_task_index[0]) # remove the task from the list
        task_listbox.delete(selected_task_index)    # remove the task from the listbox
        print(f"Task '{removed}' removed!")
    else:
        print("Please select a task to remove.")

#create the main window
root = tk.Tk()
root.title("To-Do List Manager")

#set window size
root.geometry("400x400")



# Entry widget for task input
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Create a Listbox to display tasks
task_listbox = tk.Listbox(root, height=10, width=50)  # Listbox widget to display tasks
task_listbox.pack(pady=10)

# Create Buttons for adding, removing, and viewing tasks
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)  # Button to add task
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)  # Button to remove task
remove_button.pack(pady=5)

view_button = tk.Button(root, text="View Tasks", width=20, command=view_tasks)  # Button to view tasks
view_button.pack(pady=5)

#start the tkinter event loop(this keeps the window open)
root.mainloop()



#
# while True:
#     print("\n--- To-Do List Manager ---")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Exit")
    
#     choice = input("Choose an option: ")
#     if choice == "1":
#         task = input("Enter the task: ")
#         add_task(task)
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         view_tasks()
#         try:
#             task_num = int(input("Enter the task number to remove: "))
#             remove_task(task_num)
#         except ValueError:
#             print("Please enter a valid number!")
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice, please try again.")


