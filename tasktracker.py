import argparse
import json
import datetime
import os

parser = argparse.ArgumentParser(prog = 'task-cli')
subparsers = parser.add_subparsers(dest ="action", required = True)

# Adding Actions
add_parser =  subparsers.add_parser("add")
add_parser.add_argument("destination")

list_parser =  subparsers.add_parser("list")
list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"])

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
        "status" : "todo",
        "createdAt" : dateTime,
        "updatedAt" : dateTime
    }

    tasks.append(data)

    with open('task.json', 'w') as json_file:
        json.dump(tasks, json_file, indent = 4)
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
    flag = False
    for task in tasks:
        if task["id"] == args.update_id:
            task["description"] = args.message
            task["updatedAt"] = dateTime
            with open('task.json', 'w') as json_file:
                json.dump(tasks, json_file, indent = 4)
                print(f"Task updated successfully (ID: {args.update_id})")
            flag = True
            break
    if flag == False:
        print("id not found")

# Deleting
elif args.action == "delete":
    flag = False
    for task in tasks:
        if task["id"] == args.delete_id:
            tasks.remove(task)
            with open('task.json', 'w') as json_file:
                json.dump(tasks, json_file, indent = 4)
                print(f"Task deleted successfully (ID: {args.delete_id})")
            flag = True
            break
    if flag == False:
        print("id not found")

# Marking a task as in progress
elif args.action == "mark-in-progress":
    flag = False
    for task in tasks:
        if task["id"] == args.mark_id:
            task["status"] = "in-progress"
            task["updatedAt"] = dateTime
            with open('task.json', 'w') as json_file:
                json.dump(tasks, json_file, indent = 4)
                print(f"Task mark-in-progress successfully (ID: {args.mark_id})")
            flag = True
            break
    if flag == False:
        print("id not found")

# Marking a task as done
elif args.action == "mark-done":
    flag = False
    for task in tasks:
        if task["id"] == args.mark_id:
            task["status"] = "done"
            task["updatedAt"] = dateTime
            with open('task.json', 'w') as json_file:
                json.dump(tasks, json_file, indent = 4)
                print(f"Task mark-done successfully (ID: {args.mark_id})")
            flag = True
            break
    if flag == False:
        print("id not found")

