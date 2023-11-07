# Wrapper module to make the API call to openAI's models

import os
import openai
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, "..", ".env")

load_dotenv(env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

#DAVID CODE BEGINS HERE

comment_file = "proj4test.txt" #we can switch this to a command line arg later- this is here for testing purposes

prompts = [] #creates empty list for prompts to be read by GPT

try:

    with open(comment_file, "r") as file:

        for line in file:

            prompts.append(line.strip()) #adds each line to list, omitting newline character


except FileNotFoundError:

    print("That file could not be found. Please try again.")

except Exception as e:
     
    print("Error " + e + " occurred.")


for prompt in prompts:

    print(prompt) #prints each line in file

#completion = openai.ChatCompletion.create(
    #model="gpt-3.5-turbo",
    #messages=[
        #{"role": "system", "content": "You are a modern psychiatrist, skilled in analyzing the sentiment of statements."},
        #{"role": "user", "content": "What is the sentiment of this sentence: I'm so excited!"}
        #]
    #)

#print(completion.choices[0].message)
