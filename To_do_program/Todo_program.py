# I'm going to recreate the to_do_program I made on jupyter using pycharm
# 1. for practice
# 2. To utilize Module
# 3. To get familiar and utilize git utility

import functions
import time

now = time.strftime("%c")
print("It is", now)
todos = functions.get_todos()

while True:
    user_input = input("Type add, show, edit, complete or exit: ")

    if user_input.startswith("add"):
        todo = user_input[4:]
        todos.append(todo+'\n')
        print("This is your current todo list")
        functions.show_todos(todos)

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        functions.show_todos(todos)

    elif user_input.startswith("edit"):
        edit_number = int(user_input[5:])
        new_todo = input(f"How do you want to edit {edit_number}?")
        todos[edit_number-1] = new_todo

        functions.write_todos(todos)

        print("This is your new todo list")

        functions.show_todos(todos)

    elif user_input.startswith("complete"):
        complete_number = int(user_input[9])
        print(f"You have completed {complete_number} - {todos[complete_number-1]}")
        todos.pop(complete_number-1)

        functions.write_todos(todos)

        print("This is the remaining todo list")

        functions.show_todos(todos)

    elif user_input.startswith("exit"):
        break

    else:
        print("Your input is not valid")
