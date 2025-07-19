import tkinter as tk
from tkinter import messagebox
import json
import os

# -------------------- Task Manager Class -------------------- #
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.save_tasks()

# -------------------- GUI Application -------------------- #
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.task_manager = TaskManager()

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.refresh_list()

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.task_manager.tasks):
            status = "✓" if task["done"] else "✗"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_manager.add_task(task_text)
            self.task_entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_manager.delete_task(selected[0])
            self.refresh_list()
        else:
            messagebox.showinfo("No Selection", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_manager.mark_done(selected[0])
            self.refresh_list()
        else:
            messagebox.showinfo("No Selection", "Please select a task to mark as done.")

# -------------------- Run the Application -------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
