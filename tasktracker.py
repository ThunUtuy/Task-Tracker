import argparse
import json
import datetime
import os
# Constants
TODO = "todo"
IN_PROGRESS = "in-progress"
DONE = "done"

# Functions
def save_tasks(tasks):
    with open('task.json', 'w') as json_file:
                json.dump(tasks, json_file, indent = 4)

def find_tasks(tasks, id):
    return next((task for task in tasks if task["id"] == id), None)

parser = argparse.ArgumentParser(prog = 'task-cli')
subparsers = parser.add_subparsers(dest ="action", required = True)

# Adding Actions
add_parser =  subparsers.add_parser("add")
add_parser.add_argument("destination")

list_parser =  subparsers.add_parser("list")
list_parser.add_argument("status", nargs="?", choices=[TODO, IN_PROGRESS, DONE])

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("delete_id", type=int)

update_parser = subparsers.add_parser("update")
update_parser.add_argument("update_id", type=int)
update_parser.add_argument("message")

markinprogress_parser = subparsers.add_parser("mark-in-progress")
markinprogress_parser.add_argument("mark_id", type=int)

markdone_parser = subparsers.add_parser("mark-done")
markdone_parser.add_argument("mark_id", type=int)

args = parser.parse_args()
dateTime = str(datetime.datetime.now())

if os.path.exists("task.json") and os.path.getsize("task.json") > 0:
    with open('task.json', 'r') as json_file:
            tasks = json.load(json_file)
else:
     tasks = []

# Adding a new task
if args.action == "add":
    if len(tasks) <= 0:
        id = 1
    else:
         id = max(task["id"] for task in tasks) + 1
    data = {
        "id" : id,
        "description" : args.destination,
        "status" : TODO,
        "createdAt" : dateTime,
        "updatedAt" : dateTime
    }
    tasks.append(data)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {id})")

# Listing all tasks
# Listing tasks by status
elif args.action == "list":
    if len(tasks) <= 0:
        print("No data found")
    else:
         if args.status :
              for task in tasks:
                if task["status"] ==args.status:
                    print(task["id"],task["description"])
         else:
            for task in tasks:
                s = task["status"]
                print(task["id"], task["description"], s.upper())

# Updating
elif args.action == "update":
    task = find_tasks(tasks, args.update_id)
    if task:
        task["description"] = args.message
        task["updatedAt"] = dateTime
        save_tasks(tasks)
        print(f"Task updated successfully (ID: {args.update_id})")
    else:
        print("id not found")

# Deleting
elif args.action == "delete":
    task = find_tasks(tasks, args.delete_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task deleted successfully (ID: {args.delete_id})")
    else:
        print("id not found")

# Marking a task as in progress
elif args.action == "mark-in-progress":
    task = find_tasks(tasks, args.mark_id)
    if task:
        task["status"] = IN_PROGRESS
        task["updatedAt"] = dateTime
        save_tasks(tasks)
        print(f"Task mark-in-progress successfully (ID: {args.mark_id})")
    else:
        print("id not found")

# Marking a task as done
elif args.action == "mark-done":
    task = find_tasks(tasks, args.mark_id)
    if task:
        task["status"] = DONE
        task["updatedAt"] = dateTime
        save_tasks(tasks)
        print(f"Task mark-done-progress successfully (ID: {args.mark_id})")
    else:
        print("id not found")

