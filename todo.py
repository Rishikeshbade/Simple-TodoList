import tkinter as tk

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del self.tasks[index]
            self.task_listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
