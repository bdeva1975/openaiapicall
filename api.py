import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Set the prompt
prompt = "What is the largest city in New Hampshire?"

# Create the chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    temperature=0,
    top_p=0.5,
    max_tokens=1024,
    stop=None
)

# Extract and print the response
response_text = chat_completion.choices[0].message.content
print(response_text)