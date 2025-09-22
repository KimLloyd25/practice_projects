### This is the Tax Free Childcare Calculator. ###
### This script creates a GUI application to calculate the deposit required for a tax-free childcare account. ###
### It uses the tkinter library for the GUI and allows users to input the cost of childcare. ###
### The application calculates 80% of the input cost as the required deposit for the childcare account. ###
### The code includes input validation to ensure only numeric values are entered. ###
### This is my first project utilising tkinter. ###

# #Import necessary libraries
import tkinter as tk
import tkinter.messagebox as messagebox

# Function to validate input for the cost entry field
def validate_number(P):
    # Allow empty string or only digits
    return P.isdigit() or P == ""

# Function to calculate the deposit based on the cost of childcare
def calculate_deposit():
    # Get the cost from the entry field
    cost = cost_entry.get()
    # Validate the input
    if cost == "":
        # Show an error message if the input is empty
        messagebox.showerror("Invalid Input", "Input cannot be empty. Please enter a valid number.")
        return
    # Check if the input is a valid number
    else:
        try:
            # Convert the input to a float
            cost = float(cost)
        except ValueError:
            # Show an error message if the input is not a valid number
            messagebox.showerror("Invalid Input", "Invalid input. Please enter a numeric value.")
        # Check if the cost is negative
        if cost < 0:
            # Show an error message if the cost is negative
            messagebox.showerror("Invalid Input", "Cost cannot be negative. Please enter a valid number.")
        else:
            # Calculate the deposit as 80% of the cost       
            deposit = cost * 0.8
            # Update the deposit label with the calculated deposit
            deposit_label.config(text=f"Deposit required: £{deposit:.2f}")

# Define default deposit value
deposit = 0
# Create the main application window
window = tk.Tk()
# Set the title, size, and background color of the window. Set the window to be non-resizable.
window.title("Tax Free Childcare Calculator")
window.geometry("400x350")
window.resizable(False, False)
window.configure(bg='#212121')

# Create and pack the title and instruction labels. Set their properties such as font,, text, background color, foreground color, and alignment.
title = tk.Label(window, text="Tax Free Childcare Calculator", font=("Arial", 20), bg='#212121', fg='white', anchor='center', justify='center', width=400, height=1)
instruction = tk.Label(window, text="Use this calculator to work out how much you need to deposit in to your tax free childcare account.", font=("Arial", 12), bg='#212121', fg='white', width=400, height=3, wraplength=400)
title.pack(pady=(20,0))
instruction.pack()

# Register the validation command for the cost entry field
vcmd = (window.register(validate_number), '%P')

# Create frames for the cost entry and deposit display, and pack them into the window. Set their background color.
cost_frame = tk.Frame(window, bg='#212121')
cost_frame.pack(pady=(5, 5))

# Create and pack the cost label and entry field into the cost frame.
# Set their properties such as font, text, background color, foreground color, and padding.
cost_label = tk.Label(cost_frame, text="Cost of childcare for this period:", font=("Arial", 12), bg='#212121', fg='white')
cost_entry = tk.Entry(cost_frame, font=("Arial", 12), validate='key', validatecommand=vcmd)
cost_label.pack(side='left', padx=(10, 0))
cost_entry.pack(side='left', padx=(0, 10))

# Create a frame for the deposit display and pack it into the window. Set its background color.
deposit_frame = tk.Frame(window, bg='#212121')
deposit_frame.pack(pady=(5, 5))

# Create and pack the deposit label into the deposit frame.
# Set its properties such as font, text, background color, foreground color, and padding.
deposit_label = tk.Label(deposit_frame, text=f"£{deposit}", font=("Arial", 12), bg='#212121', fg='white')
deposit_label.pack(padx=(10, 0), pady=(10, 10), anchor='s')

# Create and pack the calculate button into the window. Set its properties such as font, text, background color, foreground color, and command.
calculate_button = tk.Button(window, text="Calculate Deposit", font=("Arial", 12), command=calculate_deposit, bg='#4CAF50', fg='black')
calculate_button.pack(pady=(5, 5))

# Create and pack the disclaimer label into the window.
# Set its properties such as font, text, background color, foreground color, and wrap length.
disclaimer = tk.Label(window, text="Disclaimer: This calculator is for informational purposes only and does not constitute financial advice. You are entitled to a maximum government contribution £500 every 3 months - £2,000 per year.", font=("Arial", 9), bg='#212121', fg='white', wraplength=350)
disclaimer.pack(pady=(20, 0), padx=(5, 5), anchor='s')

# Bind the Return key to the calculate_deposit function for convenience
cost_entry.bind("<Return>", lambda event: calculate_deposit())
calculate_button.bind("<Return>", lambda event: calculate_deposit())

# Start the main event loop of the application
window.mainloop()
