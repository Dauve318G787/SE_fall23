# Wrapper module to make the API call to openAI's models

import os
import openai
import time
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, "..", ".env")
data_path = "proj4test.txt" #change this back to what you had before

load_dotenv(env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

#DAVID CODE BEGINS HERE

comments = [] #creates empty string for comments to be read by GPT
prompt = "You are a helpful psychiatrist that can analyze the sentiment of messages. Just return the sentiment of the given message" # Prompt to tell the GPT model how to behave
sentiments = []

try:

    with open(data_path, 'r', encoding='utf-8') as file:

        for line in file:

            comments.append(line.rstrip()) #adds each line to list, omitting newline character


except FileNotFoundError:

    print("That file could not be found. Please try again.")

except Exception as e:
     
    print("Error " + e + " occurred.")

comments_as_string = " ".join(comments) #converts comments list to one string

print(f"Working on {comments_as_string}")
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Analyze the sentiment of {comments_as_string}"}
    ]
)
sentiment = completion.choices[0].message
sentiments.append(sentiment)
time.sleep(21)
    
print(sentiments)
