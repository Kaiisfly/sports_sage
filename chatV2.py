import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from scrape import extract_data, data_dict
from tabulate import tabulate

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "TF_BOT"
print("Hello! Welcome to the Top Flight Basketball Academy website. Type 'quit' to exit. For Scores, enter u10_coed, "
      "u12_boys, or u14_boys")
while True:
    sentence = input('You: ')
    if sentence == "quit":
        break

    # Check if the user input matches one of the keys in the data_dict
    if sentence in data_dict:
        df = extract_data(sentence)
        if df is not None:
            print(f"{bot_name}: Here are the standings:\n{tabulate(df, headers='keys', tablefmt='psql')}")
        else:
            print(f"{bot_name}: Sorry, I couldn't retrieve the data.")
    else:
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]
        # probability
        probs = torch.softmax(output, dim=1)
        # Actual Probability
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: I do not understand. Please try rephrasing your question. If you are running into "
                  f"problems please email tf.admin@gmail.com")
