import json
from datetime import datetime

# ==== COLORS ====
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

FILE = "tasks.json"

def banner():
    print(CYAN + """
         SIMPLE  TO-DO  MANAGER
""" + RESET)

def load_task():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return tasks[-1]["Id"] + 1

def add_task():
    tasks = load_task()
    title = input("Enter Task: ").strip()
    if not title:
        print(RED + "Please enter a valid task." + RESET)
        return

    category = input("Category (work/study/personal): ").strip()
    priority = input("Priority (low/medium/high): ").strip().lower()

    new_task = {
        "Id": generate_id(tasks),
        "Title": title,
        "Category": category,
        "Priority": priority,
        "Done": False,
        "CreatedOn": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(GREEN + "Task Added!" + RESET)

def view_task():
    tasks = load_task()
    if not tasks:
        print(YELLOW + "No tasks yet." + RESET)
        return

    print("\n" + CYAN + "ID | Title | Status | Category | Priority | CreatedOn" + RESET)
    print("-" * 70)

    for t in tasks:
        status = GREEN + "✔" + RESET if t["Done"] else RED + "✖" + RESET
        print(f"{t['Id']} | {t['Title']} | {status} | {t['Category']} | {t['Priority']} | {t['CreatedOn']}")

def mark_done():
    tasks = load_task()
    try:
        tid = int(input("Enter ID: ").strip())
    except:
        print(RED + "Invalid ID." + RESET)
        return

    for t in tasks:
        if t["Id"] == tid:
            t["Done"] = True
            save_tasks(tasks)
            print(GREEN + "Marked Done!" + RESET)
            return

    print(RED + "Task Not Found." + RESET)

def delete_task():
    tasks = load_task()
    try:
        tid = int(input("Enter ID: ").strip())
    except:
        print(RED + "Invalid ID." + RESET)
        return

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm != "y":
        print(YELLOW + "Canceled." + RESET)
        return

    tasks = [t for t in tasks if t["Id"] != tid]
    save_tasks(tasks)
    print(RED + "Task Deleted!" + RESET)

def main():
    banner()
    while True:
        print(CYAN + "\n1. Add Task" + RESET)
        print(CYAN + "2. View Task" + RESET)
        print(CYAN + "3. Mark Done" + RESET)
        print(CYAN + "4. Delete Task" + RESET)
        print(CYAN + "5. Exit" + RESET)

        ch = input("Choose: ").strip()
        if ch == "1":
            add_task()
        elif ch == "2":
            view_task()
        elif ch == "3":
            mark_done()
        elif ch == "4":
            delete_task()
        elif ch == "5":
            print(GREEN + "Exiting..." + RESET)
            break
        else:
            print(RED + "Invalid choice." + RESET)

main()