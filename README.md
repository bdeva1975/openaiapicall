OpenAI API Integration with Python
This is a simple Python program that interacts with OpenAI's GPT-3.5-turbo model to generate a response for a user-defined prompt. The program uses environment variables to securely store the OpenAI API key, which is loaded via a .env file.
Features
•	Initializes OpenAI using an API key stored in a .env file.
•	Sends a custom prompt to OpenAI's GPT-3.5-turbo model.
•	Receives a response from the model and prints it to the console.
Prerequisites
•	Python 3.6+
•	An OpenAI account with access to GPT-3.5-turbo.
•	A valid OpenAI API key.
Dependencies
The following libraries are required for this project:
•	openai: The OpenAI Python client library.
•	python-dotenv: For loading environment variables from a .env file.
You can install these dependencies using pip:
bash
Copy code
pip install openai python-dotenv
How to Run the Program
1.	Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/bdeva1975/openaiapicall.git
2.	Navigate to the project directory:
bash
Copy code
cd your-repository
3.	Create a .env file in the root of your project directory and add your OpenAI API key:
makefile
Copy code
OPENAI_API_KEY=your-openai-api-key
4.	Run the Python script:
bash
Copy code
python script.py
How the Program Works
1.	Load API Key: The program first loads environment variables from a .env file using the python-dotenv package. This keeps the OpenAI API key secure and outside the main codebase.
2.	Set Up OpenAI Client: Using the OpenAI Python client, the program initializes the API connection with the provided key.
3.	Create Prompt: The program defines a prompt asking "Where is Shillong located in the world?".
4.	Generate Response: It sends the prompt to OpenAI’s GPT-3.5-turbo model, which generates a response based on the prompt.
5.	Output the Response: The model's response is extracted and printed to the console.
Example Output
csharp
Copy code
Shillong is located in northeastern India. It is the capital of the state of Meghalaya and is situated in the Khasi Hills. Shillong is known for its scenic beauty, pleasant climate, and rich cultural heritage.
Customization
You can easily change the prompt to ask anything by modifying the prompt variable in the code. The model used is gpt-3.5-turbo, but it can be replaced with any other OpenAI model depending on your access.
License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.
________________________________________
This program demonstrates how to integrate OpenAI's powerful language model with Python, allowing you to ask questions and receive intelligent responses dynamically.
