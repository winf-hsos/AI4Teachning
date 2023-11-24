# Applications of AI in Teaching

## Usage

All AI tools that depend on OpenAI's API need access to a valid API key. Make sure you have the environement variable `OPENAI_API_KEY` set to your API key. You can do this from your Python program with the following code:

```python
import os
os.environ["OPENAI_API_KEY"] = "..."
```

Make sure to replace `...` with your API key.

## Tools and how to use them

### ChatGPT

To use the copy of ChatGPT you can run the following code:

```python
from ai4teaching import ChatGPTAssistant
import os

os.environ["OPENAI_API_KEY"] = "..."
chatgpt = ChatGPTAssistant("config.json")

prompt = input("User: ")

while prompt != "exit":
    response = chatgpt.chat(prompt, model_display_name="GPT-4")
    print(f"ChatGPT: {response[-1]['content']}")
    prompt = input("User: ")
```

The `config.json` must exist, but it is sufficient to provide an empty JSON object `{}`. Here is an example:

```json
{}
```	
