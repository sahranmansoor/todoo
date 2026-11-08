import json

def main():
    todos = []
    try:
        with open("todo.txt", "r") as f:
            if f:
                todos = json.load(f)
    except FileNotFoundError, json.decoder.JSONDecodeError:
        pass


    while(True):
        cmd = input("/")

        match cmd:
            case "add":
                while(True):
                    t = input("> ")
                    if t != "done":
                        todos.append(t)
                    else:
                        break
            case "list":
                for i, t in enumerate(todos):
                    print(i+1, " ", t)
            case "del":
                while(True):
                    for i, t in enumerate(todos):
                        print(i+1, " ", t)

                    i = input("# ")
                    if i != "done":
                        if int(i) < len(todos):
                            todos.pop(int(i)-1)
                    else:
                        break
            case "exit":
                with open("todo.txt", "w") as file:
                    json.dump(todos, file)
                break

if __name__ == "__main__":
    main()
