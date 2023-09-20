import tkinter as tk

class KronosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kronos System")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.configure(bg="#192e2a")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.exit_app)
        self.root.bind("<Up>", self.select_option_up)
        self.root.bind("<Down>", self.select_option_down)
        self.root.config(cursor="none")  # Hide the mouse cursor
        
        self.password_entry = tk.Entry(self.root, font=("Impact", 20, "bold"), fg="#192e2a", bg="#f2fcfa", justify="center")
        self.password_entry.insert(0, "PASSWORD")
        self.password_entry.bind("<FocusIn>", self.on_focus_in)
        self.password_entry.bind("<Key>", self.on_key_press)
        self.password_entry.bind("<Return>", self.check_password)
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", width=self.root.winfo_screenwidth())
        self.password_entry.focus_set()  # Automatically focus the password entry
        
        self.options = ["ISLAND OPERATIONS", "FINANCES", "OMNIDROID METATRINING", "SUPERS"]
        self.selected_option = 0
        self.option_labels = []

    def on_focus_in(self, event):
        if self.password_entry.get() == "PASSWORD":
            self.password_entry.delete(0, "end")

    def on_key_press(self, event):
        if self.password_entry.get() == "PASSWORD":
            self.password_entry.delete(0, "end")

    def check_password(self, event):
        if self.password_entry.get() == "KRONOS":
            self.password_entry.destroy()
            self.border = tk.Frame(self.root, bg="#f2fcfa", bd=10)
            self.border.place(relx=0.5, rely=0.5, anchor="center", width=self.root.winfo_screenwidth(), height=320)
            self.display_options()
        else:
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, "INCORRECT")
            self.password_entry.config(fg="#D6294A")
            self.root.after(5000, self.reset_password_entry)

    def reset_password_entry(self):
        self.password_entry.config(fg="#192e2a")
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, "PASSWORD")

    def display_options(self):
        for idx, option in enumerate(self.options):
            color = "#7ee6d2" if idx == self.selected_option else "green"
            label = tk.Label(self.root, text=option, font=("Impact", 20, "bold"), fg=color, bg="#192e2a")
            label.place(relx=0.5, rely=0.4 + idx*0.1, anchor="center")
            self.option_labels.append(label)

    def select_option_up(self, event):
        if self.option_labels:
            self.selected_option = (self.selected_option - 1) % len(self.options)
            self.update_option_colors()

    def select_option_down(self, event):
        if self.option_labels:
            self.selected_option = (self.selected_option + 1) % len(self.options)
            self.update_option_colors()

    def update_option_colors(self):
        for idx, label in enumerate(self.option_labels):
            color = "#7ee6d2" if idx == self.selected_option else "green"
            label.config(fg=color)

    def exit_app(self, event):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = KronosApp(root)
    root.mainloop()
