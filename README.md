# ChatJM

This is a very basic version of ChatGPT. I made it mostly through the guidance of ChatGPT. It's an experiment on how far I can go with just (mostly) relying on ChatGPT to get information on how to write this application. Before writing this I did not know how to write code in Python, though I am a (mediocre) programmer by profession.

## How to run this application

After cloning this application, go to the folder where it is located and enter this command in the terminal to start the virtual environment:

`source myenv/bin/activate`

Then enter this to begin the application:

`python main.py`

The application will ask you to enter a question. Type in your question and then press enter. After you get a response, you can continue asking questions by entering "y" when asked to continue.

To quit, enter "n" instead.

Take note that unlike the official ChatGPT web app, the AI in this application will not remember previous questions and answers, so you won't be able to prime it or ask follow-up questions. This will be done in a different version.

## ChatGPT details

This application uses the `gpt-3.5-turbo` model mainly because it's the cheapest one to use!

The application starts with a system message that tells ChatGPT to respond concisely, which is why you may get very short answer. Just ask it to give more details when asking your questions if you want a more detailed response.

Finally, the app is using chat completion mode, which is in beta. So, I suppose there might be some bugs.