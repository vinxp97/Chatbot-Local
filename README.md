# Main.py

This is the main Python file for the Perplexity Bot project.

## Description

The `main.py` file is the entry point of the Perplexity Bot. It contains the main API logic utilizing the OpenAI API. This includes initializing the bot, setting up the necessary configurations, and starting the bot's event loop.

The file interacts with various other modules and components of the project to perform tasks such as processing user inputs, generating responses, and managing the bot's state.

## To-Do:
- Add user input() and a while-loop to keep long-form conversations
- Append context to the messages so that conversations extend beyond one single message
- Add a menu UI that allows users to 
    1) start a new conversation, 
    2) save conversation, 
    3) clear conversation, 
    4) restore previous conversation(s)
    5) adjust the selected model mid-conversation
    6) save all conversation history to a text file
    7) switch to use LangChain connectors for Agent abilities
    8) Add Llamaindex for file-indexing/semantic search using local Chromadb & local embedding model
    9) Add special token that indicates a need for semantic search 
    10) Add LM Studio option to interface with local models

## Usage

To run the Perplexity Bot, execute the following command in your terminal:

```sh
python main.py

