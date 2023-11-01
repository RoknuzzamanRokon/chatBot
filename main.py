import tkinter as tk
import openai

API_KEY = open("secret_key.txt", "r").read()
openai.api_key = API_KEY

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_2 = "#049148"

chapter_str_save = ""


def get_user_input():
    chapter = chapter_input_entry.get()
    user_question = user_input_entry.get()
    age = age_input_entry.get()
    # langauge = langauge_input_entry.get()
    dropdown_value = selected_dropdown.get()
    dropdown_value_langauge = selected_dropdown_for_langauge.get()

    age_massage = "I am " + age + " years old. "
    langauge_massage = " Using " + dropdown_value_langauge + " langauge."

    user_result = ("Give me a dictionary.where key=1,value=string.string values is give me " + chapter +
                   " chapters heading for " + user_question + langauge_massage)
    test_model = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user",
                                                         "content": user_result}])

    # result_of_title = test_model.choices[0].message.content

    try:
        dictionary = eval(result_of_title)
        if isinstance(dictionary, dict):

            # print(dictionary)
            # print(type(dictionary))
            # dic_result = dictionary[1]
            # print(dic_result)

            chapter_explanations = []

            for i in range(1, len(dictionary) + 1):
                per_chapter = dictionary[i]
                chapter_explanations.append(f"chapter-{i}>>>>>{per_chapter} \n")

                result = per_chapter + " explain it in 1000 words."

                test_model = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": result}]
                )

                gpt_result = test_model.choices[0].message.content
                # print(gpt_result)

                chapter_explanations.append(f"{gpt_result}\n\n\n")

            print(type(chapter_explanations))

            chapter_str = "\n".join(chapter_explanations)

            global chapter_str_save
            chapter_str_save = chapter_str

            user_input_text.config(state=tk.NORMAL)  # Enable the text widget for editing
            user_input_text.delete("1.0", tk.END)  # Clear the text widget
            user_input_text.insert(tk.END, chapter_str)  # Insert the new content
            user_input_text.config(state=tk.DISABLED)  # Disable the text widget (read-only)

        else:
            print("The string does not represent a valid dictionary.")
    except Exception as e:
        print("An error occurred while converting the string to a dictionary:", e)


# global chapter_str_save
# result_to_save = chapter_str_save  # Store the result for saving


# Function to save the result to a text file
def save_result():
    global chapter_str_save
    if chapter_str_save:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(chapter_str_save)
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


# # Add label for story word.
# words_label = tk.Label(window, text="How many words, do you want in the story?", font=("Arial", 20, "bold"))
# words_label.pack(pady=10)
# # Entry user word input.
# words_input_entry = tk.Entry(window, font=("Arial", 14), width=50)
# words_input_entry.pack(padx=10, pady=10)


# Dropdown Menu
dropdown_label = tk.Label(window, text="Select a Category", font=("Arial", 20, "bold"), width=30, bg=BACKGROUND_COLOR_2)
dropdown_label.pack(pady=10)

# Dropdown Options
options = ["None", "Fiction", "Non-Fiction", "Educational", "Historical"]
selected_dropdown = tk.StringVar()
selected_dropdown.set(options[0])  # Set the default selected option

dropdown_menu = tk.OptionMenu(window, selected_dropdown, *options)
dropdown_menu.pack()


# Dropdown Menu for langauge.
dropdown_label_for_langauge = tk.Label(window, text="Select a Langauge", font=("Arial", 20, "bold"), width=30,
                                       bg=BACKGROUND_COLOR_2)
dropdown_label_for_langauge.pack(pady=10)

# Dropdown Options
langauge_options = ["None", "English", "Germany"]
selected_dropdown_for_langauge = tk.StringVar()
selected_dropdown_for_langauge.set(langauge_options[0])  # Set the default selected option

dropdown_menu_langauge = tk.OptionMenu(window, selected_dropdown_for_langauge, *langauge_options)
dropdown_menu_langauge.pack()


# Add label for chapter.
chapter_label = tk.Label(window, text="How many chapters do you want?", font=("Arial", 20, "bold"), width=30,
                         bg=BACKGROUND_COLOR_2)
chapter_label.pack(pady=10)
# Entry user chapter input.
chapter_input_entry = tk.Entry(window, font=("Arial", 14), width=46)
chapter_input_entry.pack(padx=10, pady=10)

# Add label for age.
age_label = tk.Label(window, text="How older you.", font=("Arial", 20, "bold"), width=30, bg=BACKGROUND_COLOR_2)
age_label.pack(padx=10, pady=10)
# Entry for age.
age_input_entry = tk.Entry(window, font=("Arial", 14), width=46)
age_input_entry.pack(padx=10,pady=10)


# # Add label for langauge.
# langauge_label = tk.Label(window, text="Which langauge do you want to know?", font=("Arial", 20, "bold"))
# langauge_label.pack(padx=10, pady=10)
# # Entry for langauge.
# langauge_input_entry = tk.Entry(window, font=("Arial", 14), width=30)
# langauge_input_entry.pack(padx=10,pady=10)


# Add label for user question.
label = tk.Label(window, text="What story do you want to know?", font=("Arial", 20, "bold"), width=30,
                 bg=BACKGROUND_COLOR_2)
label.pack(pady=10)
# Entry widget to take user input
user_input_entry = tk.Entry(window, font=("Arial", 14), width=46)
user_input_entry.pack(padx=10, pady=10)


# Button to update the card with user input
search_button = tk.Button(window, text="Search", command=get_user_input)
search_button.pack(pady=10)

# Button to save the result
save_button = tk.Button(window, text="Save", command=save_result)
save_button.pack(pady=10)

result_to_save = None

window.mainloop()


