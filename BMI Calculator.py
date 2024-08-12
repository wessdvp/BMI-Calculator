import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height == 0:
            result_label.config(text="Error: Height cannot be zero!")
            bar_canvas.delete("all")
        else:
            bmi = weight / (height ** 2)
            result_label.config(text=f"BMI: {bmi:.2f}")
            update_bar(bmi)
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")
        bar_canvas.delete("all")


def update_bar(bmi):
    bar_canvas.delete("all")

    # Define BMI ranges and colors
    ranges = [(18.5, 24.9, "green"), (25, 29.9, "yellow"), (30, 40, "orange"), (40, 50, "red"), (50, float('inf'), "brown")]

    # Find the color based on the BMI value
    for min_bmi, max_bmi, color in ranges:
        if min_bmi <= bmi < max_bmi:
            bar_color = color
            break
    else:
        bar_color = "grey"  # Default color if BMI is out of range

    # Draw the bar

    # Adjust the bar width calculation to handle higher BMI values
    if bmi < 50:
        bar_width = 280 * (bmi - 10) / 40  # Normal scaling for BMI < 50
    else:
        bar_width = 280  # Full width for BMI >= 50

    bar_canvas.create_rectangle(10, 10, 10 + bar_width, 50, fill=bar_color, outline="black")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place the weight label and entry
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

# Create and place the height label and entry
height_label = tk.Label(window, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Create and place the BMI range bar
bar_canvas = tk.Canvas(window, width=300, height=60, bg="white")
bar_canvas.pack()

# Run the application
window.mainloop()
