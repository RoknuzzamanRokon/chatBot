import tkinter as tk
import openai

API_KEY = open("secret_key.txt", "r").read()
openai.api_key = API_KEY


user_result = ("Give me a dictionary.where key=1,value=string.string values is give me 10 chapters heading for "
               "islam")
test_model = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "user",
                                                    "content": user_result}])

result_of_title = test_model.choices[0].message.content

try:
    dictionary = eval(result_of_title)
    if isinstance(dictionary, dict):

        print(dictionary)
        print(type(dictionary))
        dic_result = dictionary[1]
        print(dic_result)
        chapter_explanations = []

        for i in range(1, len(dictionary) + 1):
            per_chapter = dictionary[i]
            result = per_chapter + " explain it in 500 words."

            test_model = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": result}]
            )

            gpt_result = test_model.choices[0].message.content
            print(gpt_result)

            chapter_explanations.append(gpt_result)

        print(chapter_explanations)

    else:
        print("The string does not represent a valid dictionary.")
except Exception as e:
    print("An error occurred while converting the string to a dictionary:", e)

