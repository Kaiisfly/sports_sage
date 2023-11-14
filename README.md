#SportsSage Basketball Academy Chatbot

![Top Flight Basketball Academy Logo](tf_logo.png)

Welcome to the SportsSage Basketball Academy Chatbot! This chatbot uses Natural Language Processing (NLP) to understand and respond to various user inputs. It also includes a web scraping feature to provide information about different basketball leagues.

Setup
Prerequisites:
You'll need Python 3.7 or later installed on your computer. You'll also need the following Python libraries:

PyTorch
NLTK
Beautiful Soup
Pandas
You can install these using pip:

shell
Copy
pip install torch nltk beautifulsoup4 pandas
Running the Chatbot:
The chatbot can be run from the command line. Navigate to the directory containing the chatbot files and run the following command:

shell
Copy
python chat.py
Overview
The chat.py script is the main script that runs the chatbot. Here's a brief overview of how it works:

The script begins by importing the necessary modules and setting up the device for PyTorch computations.
It then loads the trained model and the intents from a JSON file.
The chatbot enters into a while loop, where it waits for user input. If the input is "quit", it breaks the loop and the chatbot stops.
If the input matches one of the keys in the data dictionary, it will scrape
the format should be good with .md

GPT-4
GPT-4

Poe
SportsSage Basketball Academy Chatbot
Welcome to the SportsSage Basketball Academy Chatbot! This chatbot uses Natural Language Processing (NLP) to understand and respond to various user inputs. It also includes a web scraping feature to provide information about different basketball leagues.

Setup
Prerequisites:
You'll need Python 3.7 or later installed on your computer. You'll also need the following Python libraries:

PyTorch
NLTK
Beautiful Soup
Pandas
You can install these using pip:

bash
Copy
pip install torch nltk beautifulsoup4 pandas
Running the Chatbot:
The chatbot can be run from the command line. Navigate to the directory containing the chatbot files and run the following command:

bash
Copy
python chat.py
Overview
The chat.py script is the main script that runs the chatbot. Here's a brief overview of how it works:

The script begins by importing the necessary modules and setting up the device for PyTorch computations.
It then loads the trained model and the intents from a JSON file.
The chatbot enters into a while loop, where it waits for user input. If the input is "quit", it breaks the loop and the chatbot stops.
If the input matches one of the keys in the data dictionary, it will scrape the data and print the standings.
If the input does not match, it tokenizes the input and transforms it into a bag-of-words tensor. This tensor is then fed into the model which produces an output. The output is a tag that corresponds to the type of user intent.
The chatbot then selects a random response from the corresponding tag and prints it.
Web Scraping Feature
The chatbot includes a web scraping feature that uses Beautiful Soup to parse HTML and extract data from league tables. The HTML for the tables is stored in a Python dictionary, and the extract_data function takes a key from this dictionary, parses the HTML, and returns a Pandas DataFrame with the table data.

Here's the code for this feature:

python
Copy
from bs4 import BeautifulSoup
import pandas as pd
from table_html import u10_coed, u12_boys, u14_boys

data_dict = {
    'u10_coed': u10_coed,
    'u12_boys': u12_boys,
    'u14_boys': u14_boys,
}

def extract_data(data_key):
    # Code here...
Support
If you encounter any issues or have questions, please email sportsSage.admin@gmail.com.

Please enjoy using the SportsSage Basketball Academy Chatbot!
