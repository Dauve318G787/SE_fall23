# Wrapper module to make the API call to openAI's models

import os
import openai
from dotenv import load_dotenv

#######
# DATA
#######

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, "..", ".env")
data_path = os.path.join(script_dir, "..", "Data/processed/tag_dump.txt")
load_dotenv(env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")
comments = []
prompt = "You are a helpful psychiatrist that can analyze the sentiment of messages. Only return the sentiments of the given messages, delimited by %%. Format your response as comma seperated values" # Prompt to tell the GPT model how to behave
sentiments = ""
delimiter = '%% '

########
# END DATA
########

#####################
# Open tag file and store it in a list
####################

try:
    with open(data_path, 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = line.replace('\u200b', '').strip() # Maybe should clean the file before writing it out.
            if cleaned_line:
                comments.append(cleaned_line)

except FileNotFoundError:
    print("That file could not be found. Please try again.")

except Exception as e:
    print("Error " + e + " occurred.")

##############################
# Make the call to API, can use any here we used OpenAI
#############################

comments_as_string = delimiter.join(comments) # Needed to send all comments in a single request
print(f"Working on {comments_as_string}") # For debugging can remove
# See OpenAI doc for usage
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Analyze the sentiment of {comments_as_string}"}
    ]
)
sentiments = completion.choices[0].message
print(sentiments)
