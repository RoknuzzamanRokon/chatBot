import tkinter as tk
import openai

API_KEY = open("secret_key.txt", "r").read()
openai.api_key = API_KEY

BACKGROUND_COLOR = "#B1DDC6"


# Function to get user input
def get_user_input():
    words = words_input_entry.get()
    chapter = chapter_input_entry.get()
    user_question = user_input_entry.get()

    user_result = "create a story that will have " + words + " words and " + chapter + " chapters for " + user_question
    test_model = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": user_result}])

    show_result = test_model.choices[0].message.content

    user_input_text.config(state=tk.NORMAL)  # Enable the text widget for editing
    user_input_text.delete("1.0", tk.END)  # Clear the text widget
    user_input_text.insert(tk.END, show_result)  # Insert the new content
    user_input_text.config(state=tk.DISABLED)  # Disable the text widget (read-only)

    global result_to_save
    result_to_save = show_result  # Store the result for saving


# Function to save the result to a text file
def save_result():
    if result_to_save:
        with open("output.txt", "w") as file:
            file.write(result_to_save)
        print("Result saved to 'output.txt'")


window = tk.Tk()
window.title("Roko chatBot")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Create a Frame for the Canvas
frame = tk.Frame(window)
frame.pack(side="left", fill="y")

# Create a Canvas widget inside the Frame.
canvas = tk.Canvas(frame, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Create a Text widget with a scrollbar.
user_input_text = tk.Text(canvas, wrap=tk.WORD, width=80, height=25, state=tk.DISABLED)
user_input_text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=user_input_text.yview)
scrollbar.pack(side="right", fill="y")
user_input_text.config(yscrollcommand=scrollbar.set)

# Add label for story word.
words_label = tk.Label(window, text="How many words do you want in the story?", font=("Arial", 20, "bold"))
words_label.pack(pady=10)

# Entry user word input.
words_input_entry = tk.Entry(window, font=("Arial", 14), width=50)
words_input_entry.pack(padx=10, pady=10)

# Add label for chapter.
chapter_label = tk.Label(window, text="How many chapters do you want?", font=("Arial", 20, "bold"))
chapter_label.pack(pady=10)

# Entry user chapter input.
chapter_input_entry = tk.Entry(window, font=("Arial", 14), width=50)
chapter_input_entry.pack(padx=10, pady=10)

# Add label for user question.
label = tk.Label(window, text="What story do you want to know?", font=("Arial", 20, "bold"))
label.pack(pady=10)

# Entry widget to take user input
user_input_entry = tk.Entry(window, font=("Arial", 14), width=50)
user_input_entry.pack(padx=10, pady=10)

# Button to update the card with user input
search_button = tk.Button(window, text="Search", command=get_user_input)
search_button.pack(pady=10)

# Button to save the result
save_button = tk.Button(window, text="Save", command=save_result)
save_button.pack(pady=10)

result_to_save = None

window.mainloop()
