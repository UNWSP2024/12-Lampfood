#Elliott Morris, 4/22/2026, Car MPG.py

import tkinter as tk

class MPGCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MPG Calculator")

        #Gallon input
        self.gallons_label = tk.Label(self.window, text="Gas tank size")
        self.gallons_label.grid(row=0, column=0, padx=10, pady=5)

        self.gallons_entry = tk.Entry(self.window)
        self.gallons_entry.grid(row=0, column=1, padx=10, pady=5)

        #Miles input
        self.miles_label = tk.Label(self.window, text="Miles on a full tank")
        self.miles_label.grid(row=1, column=0, padx=10, pady=5)

        self.miles_entry = tk.Entry(self.window)
        self.miles_entry.grid(row=1, column=1, padx=10, pady=5)

        #Calculate button
        self.calculate_button = tk.Button(self.window, text="Calculate MPG", command = self.calculate_mpg)
        self.calculate_button.grid(row=2, column=0, padx=10, pady=5)

        #Quit button
        self.quit_button = tk.Button(self.window, text="Quit", command = self.window.destroy)
        self.quit_button.grid(row=2, column=1, padx=10, pady=5)

        #Result Label
        self.result_label = tk.Label(self.window, text="MPG:")
        self.result_label.grid(row=3, column=0, columnspan= 2, padx=10, pady=5)

        self.window.mainloop()

    def calculate_mpg(self):
        gallons_text = self.gallons_entry.get()
        miles_text = self.miles_entry.get()

        if not gallons_text or not miles_text:
            self.result_label.config(text="Please fill in both fields")
            return

        try:
            gallons = float(gallons_text)
            miles = float(miles_text)
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")
            return

        if gallons < 0 or miles < 0:
            self.result_label.config(text="Please enter positive numbers")
            return

        mpg = miles / gallons
        self.result_label.config(text=f"{mpg:.2f}")

if __name__ == "__main__":
    calculator = MPGCalculator()


