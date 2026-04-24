#Elliott Morris, 4/23/2026, Long-Distance Calls.py

import tkinter as tk
from tkinter import messagebox

class PhoneCharges:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Phone Call Charges")

        # Radio button variable
        self.rate_var = tk.IntVar()
        self.rate_var.set(1)  # default selection

        # Radio buttons
        self.day_radio = tk.Radiobutton(self.window, text="Daytime ($0.02/min)", variable=self.rate_var, value=1)
        self.day_radio.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.evening_radio = tk.Radiobutton(self.window, text="Evening ($0.12/min)", variable=self.rate_var, value=2)
        self.evening_radio.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.offpeak_radio = tk.Radiobutton(self.window, text="Off-Peak ($0.05/min)", variable=self.rate_var, value=3)
        self.offpeak_radio.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        # Minutes input
        self.minutes_label = tk.Label(self.window, text="Enter minutes:")
        self.minutes_label.grid(row=3, column=0, padx=10, pady=5)

        self.minutes_entry = tk.Entry(self.window)
        self.minutes_entry.grid(row=3, column=1, padx=10, pady=5)

        # Calculate button
        self.calc_button = tk.Button(self.window, text="Calculate Charge", command=self.calculate_charge)
        self.calc_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Quit button
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.window.mainloop()

    def calculate_charge(self):
        minutes_text = self.minutes_entry.get()

        # Check for empty input
        if minutes_text.strip() == "":
            messagebox.showinfo("Error", "Please enter the number of minutes.")
            return

        # Convert to number
        try:
            minutes = float(minutes_text)
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid number.")
            return

        if minutes < 0:
            messagebox.showinfo("Error", "Minutes must be positive.")
            return

        # Determine rate
        if self.rate_var.get() == 1:
            rate = 0.02
        elif self.rate_var.get() == 2:
            rate = 0.12
        else:
            rate = 0.05

        # Calculate charge
        total = minutes * rate

        # Show result in dialog box
        messagebox.showinfo("Total Charge", f"Charge: ${total:.2f}")


# Run program
if __name__ == "__main__":
    rate_app = PhoneCharges()
