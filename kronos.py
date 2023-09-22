import tkinter as tk
from datetime import datetime, timedelta


"""
TODO:
1. Password Security:
    - Avoid storing passwords in plaintext within the code.
    - Consider using a hashing mechanism to check passwords or integrating a more secure authentication method.

2. UI/UX Enhancements:
    - Improve the user interface with images, better fonts, or animations for a more appealing look.

3. Functionality Enhancements:
    - Expand the functionality of screens like `island_operations_screen`, `finances_screen`, etc.
    - Display relevant data or add interactive elements to these screens.

4. Code Organization:
    - Refactor the code to remove redundancies, such as repeated methods (like `update_option_colors`).

5. Extendibility:
    - Organize each screen's logic into separate classes or modules for better maintainability and future additions.

6. Error Handling:
    - Implement mechanisms to handle potential issues, such as incorrect user inputs or system errors.

7. Logging:
    - Add logging to keep track of user actions, errors, or other relevant events.

8. Documentation:
    - Enhance comments and docstrings to explain the purpose and functionality of each method and class.

9. Countdown Accuracy:
    - Improve the accuracy of the countdown to specific dates (e.g., October 31, 2023).
    - Refine the method used to calculate the difference between dates.

10. Exit Option:
    - Provide a clear way for users to exit the application, such as a button or a menu option.

11. Responsive Design:
    - Ensure the GUI is adaptive and looks good on different screen sizes and resolutions.

12. Additional Features:
    - Depending on the application's purpose, consider adding features like data storage, integration with other systems, or user management capabilities.

NOTE: When working on these TODOs, ensure to provide detailed explanations and comments for each change to maintain clarity for other contributors.
"""


class KronosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kronos System")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.configure(bg="#b1f0e4")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda x: self.root.destroy())
        self.root.bind("<Up>", self.select_option_up)
        self.root.bind("<Down>", self.select_option_down)
        self.root.bind("<BackSpace>", self.reset_to_password_screen)
        self.root.bind("<Return>", self.select_current_option)
        self.root.config(cursor="none")  # Hide the mouse cursor
        self.selection_rectangle = None
        
        self.canvas = tk.Canvas(self.root, bg="#b1f0e4", bd=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.init_password_screen()

    def select_option_up(self, event):
        if self.option_labels:
            self.selected_option = (self.selected_option - 1) % len(self.options)
            self.update_option_colors()

    def select_option_down(self, event):
        if self.option_labels:
            self.selected_option = (self.selected_option + 1) % len(self.options)
            self.update_option_colors()


    def init_password_screen(self):
        self.password_entry = tk.Entry(self.canvas, font=("Impact", 20, "bold"), fg="#050908", bg="#f2fcfa", justify="center")
        self.password_entry.insert(0, "PASSWORD")
        self.password_entry.bind("<FocusIn>", self.on_focus_in)
        self.password_entry.bind("<Key>", self.on_key_press)
        self.password_entry.bind("<Return>", self.check_password)
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", width=self.root.winfo_screenwidth())
        
        # Disable the password entry for 2 seconds
        self.password_entry.config(state=tk.DISABLED)
        self.root.after(2000, self.enable_password_entry)

        self.options = ["ISLAND OPERATIONS", "FINANCES", "OMNIDROID METATRINING", "SUPERS"]
        self.selected_option = 0
        self.option_labels = []

    def enable_password_entry(self):
        self.password_entry.config(state=tk.NORMAL)
        self.password_entry.focus_set()  # Automatically focus the password entry

    def on_focus_in(self, event):
        if self.password_entry.get() == "PASSWORD":
            self.password_entry.delete(0, "end")

    def on_key_press(self, event):
        if self.password_entry.get() == "PASSWORD":
            self.password_entry.delete(0, "end")

    def check_password(self, event):
        if self.password_entry.get() == "KRONOS":
            self.password_entry.destroy()
            self.draw_background_rectangle()
            self.display_options()
        else:
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, "INCORRECT")
            self.password_entry.config(fg="#D6294A")
            self.root.after(5000, self.reset_password_entry)

    def reset_password_entry(self):
        self.password_entry.config(fg="#050908")
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, "PASSWORD")

    def draw_background_rectangle(self):
        top_y = self.root.winfo_screenheight() * 0.4 - 30
        bottom_y = self.root.winfo_screenheight() * 0.7 + 30
        self.canvas.create_rectangle(0, top_y, self.root.winfo_screenwidth(), bottom_y, fill="#ffffff", outline="#ffffff")

    def display_options(self):
        for idx, option in enumerate(self.options):
            color = "#050908" if idx == self.selected_option else "#000000"
            label = tk.Label(self.canvas, text=option, font=("Impact", 20, "bold"), fg=color, bg="#b1f0e4")
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
            color = "#050908" if idx == self.selected_option else "#000000"
            label.config(fg=color)

    def reset_to_password_screen(self, event):
        for label in self.option_labels:
            label.destroy()
        self.option_labels.clear()
        self.canvas.delete("all")
        self.init_password_screen()

    
    def update_option_colors(self):
        for idx, label in enumerate(self.option_labels):
            color = "#050908" if idx == self.selected_option else "#000000"
            label.config(fg=color)
            
            if idx == self.selected_option:
                if self.selection_rectangle:
                    self.canvas.delete(self.selection_rectangle)
                x0, y0, x1, y1 = label.bbox()
                self.selection_rectangle = self.canvas.create_rectangle(x0-10, y0-10, x1+10, y1+10, outline="#2986cc", width=2)

    def select_current_option(self, event):
        if self.selected_option == 0:
            self.island_operations_screen()
        elif self.selected_option == 1:
            self.finances_screen()
        elif self.selected_option == 2:
            self.omnidroid_metatrining_screen()
        # Add more options as needed

    def island_operations_screen(self):
        self.canvas.delete("all")
        width = self.root.winfo_screenwidth() * 0.8
        height = self.root.winfo_screenheight() * 0.8
        x = (self.root.winfo_screenwidth() - width) / 2
        y = (self.root.winfo_screenheight() - height) / 2
        self.canvas.create_rectangle(x, y, x+width, y+height, fill="#ffffff")
        self.canvas.create_text(x+width-10, y+10, text="ISLAND OPERATIONS", font=("Impact", 40, "bold"), anchor="ne")

    def finances_screen(self):
        self.canvas.delete("all")
        width = self.root.winfo_screenwidth() * 0.8
        height = self.root.winfo_screenheight() * 0.8
        x = (self.root.winfo_screenwidth() - width) / 2
        y = (self.root.winfo_screenheight() - height) / 2
        self.canvas.create_rectangle(x, y, x+width, y+height, fill="#ffffff")
        self.canvas.create_text(x+width-10, y+10, text="FINANCES", font=("Impact", 40, "bold"), anchor="ne")
        self.canvas.create_line(x, y+height/2, x+width, y+height/2, fill="#000000", width=5)

    def omnidroid_metatrining_screen(self):
        self.canvas.delete("all")
        radius = min(self.root.winfo_screenwidth(), self.root.winfo_screenheight()) * 0.4
        x = self.root.winfo_screenwidth() / 2
        y = self.root.winfo_screenheight() / 2
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#ffffff")
        
        # Display current time
        current_time = datetime.now().strftime('%H:%M:%S')
        self.canvas.create_text(x, y-30, text=current_time, font=("Impact", 40), fill="#000000")
        
        # Countdown to October 31, 2023
        target_date = datetime(2023, 10, 31)
        delta = target_date - datetime.now()
        months = delta.days // 30
        days = delta.days % 30
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_text = f"{months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        self.canvas.create_text(x, y+30, text=countdown_text, font=("Impact", 20), fill="#000000")


    def exit_app(self, event):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = KronosApp(root)
    root.mainloop()
