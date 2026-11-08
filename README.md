# CLI To-Do List

A lightweight, command-line To-Do list manager. Tasks are automatically saved to and loaded from a local `todo.txt` file using JSON formatting.

## Requirements
- **Python 3.10+** (Required for `match/case` structural pattern matching)

## Usage
Run the script from your terminal:
```bash
python todo.py
```

## Commands
Enter the following commands at the `/` prompt:

| Command | Description |
| :--- | :--- |
| `add` | Add new tasks. Enter them one by one. Type `done` to finish. |
| `list` | Display all current tasks with their index numbers. |
| `del` | Delete a task by entering its index number. Type `done` to finish. |
| `exit` | Save the current list to `todo.txt` and exit the app. |

## Example Session

```text
$ python todo.py
/ add
> Buy groceries
> Study for OS exam
> done
/ list
1   Buy groceries
2   Study for OS exam
/ del
1   Buy groceries
2   Study for OS exam
# 1
1   Study for OS exam
# done
/ exit
```
