from tkinter import *
import tkinter as tk
from tkinter import ttk

def update_conversion_methods(*args):
    selected_type = type_var.get()
    
    if selected_type == "Length":
        conversion_combobox['values'] = ("Centimeter to Meter", "Meter to Centimeter", "Centimeter to INCH", "INCH to Centimeter","Centimeter to KiloMetre","KiloMetre to Centimeter","Centimeter to FOOT","FOOT to Centimeter","Kilometre to Mile","Mile to Kilometre","Centimeter to Feets","Feet to inches")
    elif selected_type == "Mass":
        conversion_combobox['values'] = ("Gram to Kilogram", "Kilogram to Gram", "Kilogram to Tonne","Kilogram to Tonne", "Tonne to Kilogram","Milligram to Kilogram","Kilogram to Milligram","Milligram to Gram","Gram to Milligram","kilogram to pound (lb)","pound (lb) to Kilogram","Micrograms to gram","Micrograms to Kilogram")
    elif selected_type == "Temperature":
        conversion_combobox['values'] = ("Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius", "Fahrenheit to Kelvin", "Kelvin to Celsius","Kelvin to Fahrenheit")
    elif selected_type == "Time":
        conversion_combobox['values'] = ("Second to Minute", "Minute to Second", "Second to Hour", "Minute to Hour","Hour to Minute","Day to Hour","Hour to Day")
    elif selected_type == "Speed":
        conversion_combobox['values'] = ("Mile per hour to kilometer per hour", "Kilometer per hour to Mile per hour", "Mile per hour to Meter per Second", "Meter per Second to Mile per hour","Kilometer per hour to Meter per Second","Meter per Second to Kilometer per hour")
    elif selected_type == "Energy":
        conversion_combobox['values'] = ("Joule to Kilojoule", "Kilojoule to Joule", "Joule to Kilocalorie", "Kilocalorie to Joule","Kilojoule to Kilocalorie","Kilocalorie to Kilojoule")
    elif selected_type == "Pressure":
        conversion_combobox['values'] = ("Bar to Pascal", "Bar to Standard atmosphere", "Pascal to Bar", "Pascal to Standard atmosphere","Standard atmosphere to Pascal","Standard atmosphere to Bar")
    elif selected_type == "Area":
        conversion_combobox['values'] = ("Sqft to Sqmtrs", "Sqft to Hectre / Acres")
    else:
        conversion_combobox['values'] = ()  # Clear the combobox if no type is selected

# Function to perform the conversion
def convert():
    # Get the selected type of conversion
    selected_type = type_var.get()
    
    # Get the user input and convert to float
    input_value = entry.get()
    
    # Get the selected conversion method
    selected_conversion = conversion_var.get()
    
    # Default result message
    result = "Select a conversion and enter a value."
    
    if selected_type and selected_conversion and input_value:
        input_value = float(input_value)
        # Perform the conversion based on the selected type
        if selected_type == "Length":
            if selected_conversion == "Centimeter to Meter":
                result = input_value / 100
            elif selected_conversion == "Meter to Centimeter":
                result = input_value * 100
            elif selected_conversion == "Centimeter to INCH":
                result = input_value / 2.54
            elif selected_conversion == "INCH to Centimeter":
                result = input_value * 2.54
            elif selected_conversion == "Centimeter to KiloMetre":
                result = input_value / 100000
            elif selected_conversion == "KiloMetre to Centimeter":
                result = input_value * 100000
            elif selected_conversion == "Centimeter to FOOT":
                result = input_value / 30.48
            elif selected_conversion == "FOOT to Centimeter":
                result = input_value * 30.48
            elif selected_conversion == "Kilometre to Mile":
                result = input_value / 1.609
            elif selected_conversion == "Mile to Kilometre":
                result = input_value * 1.609
            elif selected_conversion == "Centimeter to Feets":
                result = input_value * 0.0328084
            elif selected_conversion == "Feet to inches":
                result = input_value * 12
            
            
    
        elif selected_type == "Mass":
            if selected_conversion == "Gram to Kilogram":
                result = input_value / 1000
            elif selected_conversion == "Kilogram to Gram":
                result = input_value * 1000
            elif selected_conversion == "Kilogram to Tonne":
                result = input_value / 1000
            elif selected_conversion == "Tonne to Kilogram":
                result = input_value * 1000
            elif selected_conversion == "Milligram to Kilogram":
                result = input_value / 1000000
            elif selected_conversion == "Kilogram to Milligram":
                result = input_value * 1000000
            elif selected_conversion == "Milligram to Gram":
                result = input_value / 1000
            elif selected_conversion == "Gram to Milligram":
                result = input_value * 1000
            elif selected_conversion == "kilogram to pound (lb)":
                result = input_value * 2.20462
            elif selected_conversion == "pound (lb) to Kilogram":
                result = input_value / 2.20462
            elif selected_conversion == "Micrograms to gram":
                result = input_value / 1e+6
            elif selected_conversion == "Micrograms to Kilogram":
                result = input_value / 1e+9         
    
        
        
        elif selected_type == "Temperature":
            if selected_conversion == "Celsius to Fahrenheit":
                result = (input_value * 9.5) + 32
            elif selected_conversion == "Celsius to Kelvin":
                result = input_value + 273.15
            elif selected_conversion == "Fahrenheit to Celsius":
                result = (input_value - 32) * 5.9
            elif selected_conversion == "Fahrenheit to Kelvin":
                result = (input_value - 32) * 5.9 + 273.15
            elif selected_conversion == "Kelvin to Celsius":
                result = input_value - 273.15
            elif selected_conversion == "Kelvin to Fahrenheit":
                result = (input_value - 273.15) * 9.5 + 32
                
           
        
        elif selected_type == "Time":
            if selected_conversion == "Second to Minute":
                result = input_value / 60
            elif selected_conversion == "Minute to Second":
                result = input_value * 60
            elif selected_conversion == "Second to Hour":
                result = input_value / 3600
            elif selected_conversion == "Minute to Hour":
                result = input_value / 60
            elif selected_conversion == "Hour to Minute":
                result = input_value * 60
            elif selected_conversion == "Day to Hour":
                result = input_value * 24
            elif selected_conversion == "Hour to Day":
                result = input_value / 24
                
                
                
        elif selected_type == "Speed":
            if selected_conversion == "Mile per hour to kilometer per hour":
                result = input_value * 1.609
            elif selected_conversion == "Kilometer per hour to Mile per hour":
                result = input_value / 1.609
            elif selected_conversion == "Mile per hour to Meter per Second":
                result = input_value / 2.237
            elif selected_conversion == "Meter per Second to Mile per hour":
                result = input_value * 2.237
            elif selected_conversion == "Kilometer per hour to Meter per Second":
                result = input_value / 3.6
            elif selected_conversion == "Meter per Second to Kilometer per hour":
                result = input_value * 3.6
    
    
    
        elif selected_type == "Energy":
            if selected_conversion == "Joule to Kilojoule":
                result = input_value / 1000
            elif selected_conversion == "Kilojoule to Joule":
                result = input_value * 1000
            elif selected_conversion == "Joule to Kilocalorie":
                result = input_value / 4184
            elif selected_conversion == "Kilocalorie to Joule":
                result = input_value * 4184
            elif selected_conversion == "Kilojoule to Kilocalorie":
                result = input_value / 4.184
            elif selected_conversion == "Kilocalorie to Kilojoule":
                result = input_value * 4.184
                
                
                
        elif selected_type == "Pressure":
            if selected_conversion == "Bar to Pascal":
                result = input_value * 100000
            elif selected_conversion == "Bar to Standard atmosphere":
                result = input_value / 1.013
            elif selected_conversion == "Pascal to Bar":
                result = input_value / 100000
            elif selected_conversion == "Pascal to Standard atmosphere":
                result = input_value / 101300
            elif selected_conversion == "Standard atmosphere to Pascal":
                result = input_value * 101300
            elif selected_conversion == "Standard atmosphere to Bar":
                result = input_value * 1.013    
        
    
    
        elif selected_type == "Area":
            if selected_conversion == "Sqft to Sqmtrs":
                result = input_value * 0.09290304
            elif selected_conversion == "Sqft to Hectre / Acres":
                result = input_value * 0.0000092903
    
    # Update the result label
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create a label for the title
title_label = tk.Label(root, text="Unit Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Create a label for type selection
type_label = tk.Label(root, text="Choose the type of conversion:")
type_label.pack()

# Create a combobox for selecting the type
type_var = tk.StringVar()
type_combobox = ttk.Combobox(root, textvariable=type_var, values=("Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure","Area"))
type_combobox.pack()

# Link the update_conversion_methods function to the type_var
type_var.trace("w", update_conversion_methods)

# Create a label for value input
value_label = tk.Label(root, text="Enter a value to convert:")
value_label.pack()

# Create an entry for user input
entry = tk.Entry(root)
entry.pack()

# Create a label for conversion method selection
conversion_label = tk.Label(root, text="Choose the conversion method:")
conversion_label.pack()

# Create a combobox for selecting the conversion method
conversion_var = tk.StringVar()
conversion_combobox = ttk.Combobox(root, textvariable=conversion_var, values=())  # Start with an empty list
conversion_combobox.pack()

# Create a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Create a label for displaying the result
result_label = tk.Label(root, text="Result: Select a conversion and enter a value.")
result_label.pack()

# Start the GUI main loop
root.mainloop()
