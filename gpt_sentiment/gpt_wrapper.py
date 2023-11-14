# Wrapper module to make the API call to openAI's models

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

#######
# DATA
#######

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, "..", ".env")
data_path = os.path.join(script_dir, "..", "data/processed/tag_dump.txt")
sentiment_dest = os.path.join(script_dir, "..", "data/sentiments/sentiment_dump.txt")
load_dotenv(env_path)
#openai.api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)
prompt = "You are a helpful psychiatrist that can analyze the sentiment of messages. Only return the sentiments of the given messages, delimited by %%. Format your response as comma seperated values" # Prompt to tell the GPT model how to behave

########
# END DATA
########

#####################
# Open tag file and store it in a list
#####################
def get_processed_data(path):
    comments = []
    delimiter = '%% '
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.replace('\u200b', '').strip() # Maybe should clean the file before writing it out.
                if cleaned_line:
                    comments.append(cleaned_line)

    except FileNotFoundError:
        print("That file could not be found. Please try again.")

    except Exception as e:
        print("Error " + e + " occurred.")

    comments_as_string = delimiter.join(comments) # Needed to send all comments in a single request
    return comments_as_string
    
##############################
# Make the call to API, can use any here we used OpenAI
#############################
def request_sentiment(user_prompt, prompt_content):
    sentiments = ""
    #print(f"Working on {prompt_content}") # For debugging can remove
    # See OpenAI doc for usage
    assistant = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": prompt_content}
        ]
    )
    sentiments = assistant.choices[0].message.content
    return sentiments

###########################
# Write the sentiments out to a file
###########################
def write_sentiment():
    analysis = request_sentiment(prompt, get_processed_data(data_path))
    try:
        with open(sentiment_dest, 'w', encoding='utf-8') as file:
            file.write(analysis)
            file.write("\n")
            print(f"Sentiments written to {sentiment_dest}")

    except Exception as e:
        print("Error " + e + " has occured")
