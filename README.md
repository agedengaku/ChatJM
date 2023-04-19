# ChatJM

This is a very basic version of ChatGPT. I made it mostly through the guidance of ChatGPT. It's an experiment on how far I can go with just (mostly) relying on ChatGPT to get information on how to write this application. Before writing this I did not know how to write code in Python, though I am a (mediocre) programmer by profession.

## How to run this application

First, you'll need to get a ChatGPT API key. Visit this page for more information: https://platform.openai.com/overview

Next, clone this application and go to the folder where it is located.

Enter this command in the terminal to create your own `.env` file:

`cp .env-example .env`

Open the new `.env` file and replace the text `place_your_api_key_here` with your API key. Then save the file.

After that, enter this command to start the virtual environment:

`source myenv/bin/activate`

And then run this to begin the application:

`python main.py`

The application will ask you to enter a question. Type in your question and press enter. After you get a response, you can continue asking questions by entering "y" when asked to continue.

To quit, enter "n" instead.

You can now ask follow-up questions. After asking your first question, your second question can be related to the first one, and ChatGPT should respond accordingly.

## ChatGPT details

This application uses the `gpt-3.5-turbo` model mainly because it's the cheapest one to use!

The application starts with a system message that tells ChatGPT to respond concisely, which is why you may get very short answer. If you want a more detailed response, just let the AI know when asking your questions.

Finally, the app is using chat completion mode, which is in beta. So, I suppose there might be some bugs.
