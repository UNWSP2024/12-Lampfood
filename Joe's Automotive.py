#Elliott Morris, 4/23/2026, Joe's Automotive.py

import tkinter as tk

class AutoShopGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Joe's Automotive")

        # Variables
        self.oil_var = tk.IntVar()
        self.lube_var = tk.IntVar()
        self.radiator_var = tk.IntVar()
        self.transmission_var = tk.IntVar()
        self.inspection_var = tk.IntVar()
        self.muffler_var = tk.IntVar()
        self.tire_var = tk.IntVar()

        # Checkbuttons
        self.oil_cb = tk.Checkbutton(self.window, text="Oil Change - $30", variable=self.oil_var)
        self.oil_cb.grid(row=0, column=0, sticky="w")

        self.lube_cb = tk.Checkbutton(self.window, text="Lube Job - $20", variable=self.lube_var)
        self.lube_cb.grid(row=1, column=0, sticky="w")

        self.radiator_cb = tk.Checkbutton(self.window, text="Radiator Flush - $40", variable=self.radiator_var)
        self.radiator_cb.grid(row=2, column=0, sticky="w")

        self.transmission_cb = tk.Checkbutton(self.window, text="Transmission Fluid - $100", variable=self.transmission_var)
        self.transmission_cb.grid(row=3, column=0, sticky="w")

        self.inspection_cb = tk.Checkbutton(self.window, text="Inspection - $35", variable=self.inspection_var)
        self.inspection_cb.grid(row=4, column=0, sticky="w")

        self.muffler_cb = tk.Checkbutton(self.window, text="Muffler Replacement - $200", variable=self.muffler_var)
        self.muffler_cb.grid(row=5, column=0, sticky="w")

        self.tire_cb = tk.Checkbutton(self.window, text="Tire Rotation - $20", variable=self.tire_var)
        self.tire_cb.grid(row=6, column=0, sticky="w")

        # Calculate button
        self.calc_button = tk.Button(self.window, text="Calculate Total", command=self.calculate_total)
        self.calc_button.grid(row=7, column=0, columnspan=2, pady=5)


        # Quit button
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        self.quit_button.grid(row=8, column=0, columnspan=2, pady=5)

        # Result label
        self.result_label = tk.Label(self.window, text="Total: $0.00")
        self.result_label.grid(row=9, column=0, columnspan=2, pady=5)

        self.window.mainloop()

    def calculate_total(self):
        total = 0

        if self.oil_var.get() == 1:
            total += 30
        if self.lube_var.get() == 1:
            total += 20
        if self.radiator_var.get() == 1:
            total += 40
        if self.transmission_var.get() == 1:
            total += 100
        if self.inspection_var.get() == 1:
            total += 35
        if self.muffler_var.get() == 1:
            total += 200
        if self.tire_var.get() == 1:
            total += 20

        self.result_label.config(text=f"Total: ${total:.2f}")

# Run program
if __name__ == "__main__":
    shop = AutoShopGUI()
