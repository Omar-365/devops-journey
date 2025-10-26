import sqlite3
import time

DB_FILE = "tasks.db"

# -----------------------------
# 1. Database setup
# -----------------------------
def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            command TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

# -----------------------------
# 2. Add task
# -----------------------------
def add_task(name, command):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (name, command, status) VALUES (?, ?, 'pending')", (name, command))
    conn.commit()
    conn.close()
    print(f" Task '{name}' added successfully!\n")

# -----------------------------
# 3. View all tasks
# -----------------------------
def view_tasks():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, name, command, status FROM tasks ORDER BY id")
    tasks = cur.fetchall()
    conn.close()

    if not tasks:
        print(" No tasks found.\n")
        return

    print("\n All Tasks:")
    print("-" * 40) # -----------------------------
    for task_id, name, command, status in tasks:
        print(f"[{task_id}] {name} | {command} | {status}")
    print("-" * 40, "\n") #_# -----------------------------


# 4. Get pending tasks
# -----------------------------
def get_pending_tasks():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, name, command FROM tasks WHERE status='pending'")
    tasks = cur.fetchall()
    conn.close()
    return tasks

# -----------------------------
# 5. Run tasks
# -----------------------------
def run_tasks():
    tasks = get_pending_tasks()
    if not tasks:
        print(" No pending tasks to run.\n")
        return

    for task_id, name, command in tasks:
        print(f" Running: {name} -> {command}")
        time.sleep(1)  # simulate work
        print(f" Done: {name}")
        mark_task_done(task_id)
    print("\n All pending tasks have been completed!\n")

def mark_task_done(task_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status='done' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

# -----------------------------
# 6. Menu
# -----------------------------
def menu():
    while True:
        print("==== Simple Task Runner ====")
        print("1. View all tasks")
        print("2. Add new task")
        print("3. Run pending tasks")
        print("4. Exit")
      
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            name = input("Enter task name: ").strip()
            command = input("Enter command (e.g., copy file.txt): ").strip()
            add_task(name, command)
        elif choice == "3":
            run_tasks()
        elif choice == "4":
            print(" Exiting... Bye!")
            break
        else:
            print(" Invalid choice. Try again.\n")

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    setup_db()
    menu()
####################

# ==== Simple Task Runner ====
# 1. View all tasks
# 2. Add new task
# 3. Run pending tasks
# 4. Exit
# ============================

----------------------------------------------
| id |     name     |    command   |  status |
----------------------------------------------
| 1  | Read DB       | read db      | done    |
| 2  | Copy Logs     | copy logs.txt| pending |
| 3  | Cleanup Temp  | delete temp  | done    |
----------------------------------------------



# # Ho to run it 
# python final_project.py

# import task_runner
