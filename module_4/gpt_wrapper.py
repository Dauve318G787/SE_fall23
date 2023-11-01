# Wrapper module to make the API call to openAI's models

import os
import openai
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath("gpt_wrapper.py"))
env_path = os.path.join(script_dir, "..", ".env")

load_dotenv(env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a modern psychiatrist, skilled in analyzing the sentiment of statements."},
        {"role": "user", "content": "What is the sentiment of this sentence: I'm so excited!"}
        ]
    )

print(completion.choices[0].message)
