import tkinter as tk  
from tkinter import ttk  
from tkinter import messagebox  

class Timer:
    def __init__(self, root):
        self.root = root  # Reference to the root window
        self.root.title("Timer using Python")  
        self.root.geometry("500x500")  

        self.time = 0  # Initialize the timer value
        self.running = False  # Initialize the running state
        self.mode = "stopwatch"  
        self.countdown_time = 60  
        self.root.configure(bg="lightblue")  

        # Create a label to display the time
        self.label = tk.Label(self.root, text="00:00:00", pady=20, font=("Helvetica", 35), bg="lightblue", fg="black")
        self.label.pack() 

        # Style the buttons
        style = ttk.Style()  # Create a style object
        style.configure("TButton", font=("Helvetica", 15), background="red", foreground="black", padding=10)  # Configure the button style
        style.map("TButton", background=[('active', 'yellow')])  # Change button background color when active

        # Create and pack the start,stop,reset button
        self.start_button = ttk.Button(self.root, text="Start", width=10, command=self.start)
        self.start_button.pack(pady=5)  # Add padding around the button
        self.stop_button = ttk.Button(self.root, text="Stop", width=10, command=self.stop)
        self.stop_button.pack(pady=5) 
        self.reset_button = ttk.Button(self.root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(pady=5)  
        # Create and pack the mode switch button
        self.mode_button = ttk.Button(self.root, text="Switch to Countdown", width=20, command=self.switch_mode)
        self.mode_button.pack(pady=5)  

    def start(self):
        if not self.running:  
            self.running = True  
            self.count()  

    def stop(self):
        self.running = False  

    def reset(self):
        self.running = False  
        self.time = 0 if self.mode == "stopwatch" else self.countdown_time  # Reset the timer based on the mode
        self.update_label()  # Update the time label

    def switch_mode(self):
        self.stop() 
        self.reset()  
        if self.mode == "stopwatch":  
            self.mode = "countdown"  # Switch to countdown mode
            self.mode_button.config(text="Switch to Stopwatch")  # Update the mode button text
            self.time = self.countdown_time  
        else:  
            self.mode = "stopwatch"  
            self.mode_button.config(text="Switch to Countdown")  

    def count(self):
        if self.running:  
            if self.mode == "stopwatch": 
                self.time += 1 
            elif self.mode == "countdown":  
                if self.time <= 0: 
                    self.running = False  
                    messagebox.showinfo("Time's up!", "Countdown has finished!")  # Show a message box
                    return 
                else:
                    self.time -= 1  

            self.update_label()  
            self.root.after(1000, self.count)  

    def update_label(self):
        minutes, seconds = divmod(self.time, 60) 
        hours, minutes = divmod(minutes, 60)  
        self.label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)) 

def main():
    root = tk.Tk()  # Create the main window
    app = Timer(root)  # Create an instance of the Timer class
    root.mainloop()  
main()