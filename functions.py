def write_todos(todos_arg=todos):
    with open(r'C:\Users\Leon\Desktop\jupyter\Python_Tutorial\todos.txt', 'w') as file:
        file.writelines(todos_arg)
        print("does it work?")

print("The time is below: ")