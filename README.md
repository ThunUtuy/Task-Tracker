# Task-Tracker
## What is this project
This project is a task tracker with basic functionalities (listed in the next section). You use CLI (command line interface to interact with the program). This project idea is from [roadmap.sh](https://roadmap.sh/projects/task-tracker).
## Functionalities
replace task-cli with python tasktracker.py

- Adding a new task
  - task-cli add "Buy groceries"
  - Output: Task added successfully (ID: 1)

- Updating and deleting tasks
  - task-cli update 1 "Buy groceries and cook dinner"
  - task-cli delete 1

- Marking a task as in progress or done
  - task-cli mark-in-progress 1
  - task-cli mark-done 1

- Listing all tasks
  - task-cli list

- Listing tasks by status
  - task-cli list done
  - task-cli list todo
  - task-cli list in-progress
