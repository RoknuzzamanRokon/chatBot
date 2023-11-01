import tkinter as tk


def on_option_select(*args):
    dropdown_value = selected_dropdown.get()

    print(dropdown_value)

window = tk.Tk()
window.title("Dropdown Menu Example")
# Dropdown Menu
dropdown_label = tk.Label(window, text="Select an option:", font=("Arial", 20, "bold"))
dropdown_label.pack(pady=10)

# Dropdown Options
options = ["x", "y", "z"]
selected_dropdown = tk.StringVar()
selected_dropdown.set(options[0])  # Set the default selected option

dropdown_menu = tk.OptionMenu(window, selected_dropdown, *options)
dropdown_menu.pack()

window.mainloop()
