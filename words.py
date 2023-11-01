import openai

# Set your OpenAI API key
api_key = open("secret_key.txt", "r").read()
openai.api_key = api_key

# Define a prompt to generate a list of key-value pairs
prompt = "Create a dictionary with 5 chapters for an cristiano Ronaldo."

# Use ChatGPT to generate the key-value pairs
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You are a helpful assistant that generates a dictionary."},
              {"role": "user", "content": prompt}],
    max_tokens=100,  # Adjust max_tokens as needed
)

# Extract the generated text
generated_text = response.choices[0].message.content
print(generated_text)

# Manually format the generated text into a Python dictionary
lines = generated_text.strip().split("\n")
my_dict = {}

for line in lines:
    parts = line.split(":")
    if len(parts) >= 2:
        key = parts[0].strip()
        value = parts[1].strip()
        my_dict[key] = value

# Print the generated dictionary
print(my_dict)

# import openai
#
#
# API_KEY = open("secret_key.txt", "r").read()
# openai.api_key = API_KEY
# # Define your prompt
# prompt = "Genaret 5 chapter headding list.in islamick book"
#
# # Use ChatGPT to generate the list
# response = openai.Completion.create(
#     engine="davinci",
#     prompt=prompt,
#     max_tokens=50,  # Adjust max_tokens as needed to limit the response length
#     n = 5,  # Generate 5 completions
# )
#
# # Extract the generated list
# chapters = [completion['text'].strip() for completion in response.choices]
# print(chapters)
# # Print the generated list
# for i, chapter in enumerate(chapters, 1):
#     print(f"Chapter {i}: {chapter}")
#


















#
# # Store the explanations in a list
# chapter_explanations = []
#
# for i in range(1, len(islamic_book_chapters) + 1):
#     per_chapter = islamic_book_chapters[i]
#     result = per_chapter + " explain it in 500 words."
#     print(result)
#     test_model = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": result}]
#     )
#
#     gpt_result = test_model.choices[0].message.content
#     print(gpt_result)
#
#     chapter_explanations.append(gpt_result)
#
# print(chapter_explanations)
