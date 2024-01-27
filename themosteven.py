import tkinter as tk
from tkinter import messagebox
import threading
import time

class themosteven:
    def __init__(self, master):
        self.master = master
        self.master.title("The most even number")
        self.master.geometry("400x200")

        self.label = tk.Label(self.master, text="What is the number from 0 to a 100\n that can be divided by 2 the most times?")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="Time left: 30 seconds")
        self.timer_label.pack(pady=10)

        self.timer_thread = threading.Thread(target=self.start_timer)
        self.timer_thread.start()

    def start_timer(self):
        for i in range(30, 0, -1):
            time.sleep(1)
            self.timer_label.config(text=f"Time left: {i} seconds")
            if i == 1:
                self.timer_label.config(text="Time's up!")
                self.master.after(1000, self.timeout)

    def check_answer(self):
        try:
            user_input = int(self.entry.get())
            # Replace the following condition with your own question logic
            if user_input == 64:
                messagebox.showinfo("Correct!", "You got it right!, the number 64\n can be divided by 2 six times")
            else:
                messagebox.showerror("Incorrect", "Try again!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def timeout(self):
        self.submit_button.config(state="disabled")
        messagebox.showinfo("Time's up!", "You ran out of time!")

if __name__ == "__main__":
    root = tk.Tk()
    app = themosteven(root)
    root.mainloop()
