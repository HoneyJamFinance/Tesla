FILENAME = "todos.txt"


def get_todos(filename=FILENAME):
    with open(filename, 'r') as file:
        local_todos = file.readlines()
    return local_todos


def show_todos(todos):
    for i, content in enumerate(todos):
        content = content.capitalize()
        content = content.strip('\n')
        row = [f"{i+1}-{content}"]
        print(row)


def write_todos(todos, filename=FILENAME):
    with open(filename, "w") as file:
        file.writelines(todos)
