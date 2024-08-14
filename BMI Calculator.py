import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height == 0:
            result_label.config(text="Error: Height cannot be zero!")
            bar_canvas.delete("all")
            obesity_label.config(text="")
        else:
            bmi = weight / (height ** 2)
            result_label.config(text=f"BMI: {bmi:.2f}")
            update_bar(bmi)
            obesity_state = get_obesity_state(bmi)
            obesity_label.config(text=f"Obesity State: {obesity_state}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")
        bar_canvas.delete("all")

# obesity meter
def get_obesity_state(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Moderately obese"
    elif 35 <= bmi < 40:
        return "Severely obese"
    else:
        return "Morbidly obese"

# the bmi bar function
def update_bar(bmi):
    bar_canvas.delete("all")

    # define BMI ranges and colors
    ranges = [(0, 18.49, "blue"), (18.5, 24.99, "green"), (25, 29.99, "yellow"), (30, 34.99, "orange"), (35, 39.99, "red"), (40, float('inf'), "brown")]
    # Find the color based on the BMI value
    for min_bmi, max_bmi, color in ranges:
        if min_bmi <= bmi < max_bmi:
            bar_color = color
            break
    else:
        bar_color = "grey"  # Default color if BMI is out of range

    # draw the bar

    # adjust the bar width calculation to handle higher BMI values
    if bmi < 50:
        bar_width = 280 * (bmi - 10) / 40  # Normal scaling for BMI < 50
    else:
        bar_width = 280  # Full width for BMI >= 50

    bar_canvas.create_rectangle(10, 10, 10 + bar_width, 50, fill=bar_color, outline="black")

# create the main window
window = tk.Tk()
window.title("BMI Calculator")

# create and place the weight label and entry
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

# create and place the height label and entry
height_label = tk.Label(window, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

# create and place the calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# create and place the BMI range bar
bar_canvas = tk.Canvas(window, width=300, height=60, bg="white")
bar_canvas.pack()

# create and place the obesity state label
obesity_label = tk.Label(window, text="")
obesity_label.pack()

# run the application
window.mainloop()
