from flask import Flask, render_template, request
import pandas as pd
import difflib

app = Flask(__name__)

def read_dataset(file_path):
    skincare_responses = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '?' in line:
                question, answer = line.strip().split(',')
                skincare_responses[question.strip().lower()] = answer.strip()
    return skincare_responses

def skincare_chatbot(query, skincare_responses):
    query = query.lower()
    best_match = difflib.get_close_matches(query, skincare_responses.keys(), n=1, cutoff=0.6)
    if best_match:
        return skincare_responses[best_match[0]]
    else:
        return "I'm sorry, I'm not sure about that. Could you please ask something else?"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    dataset_file = "dataset.csv"  # Assuming dataset.csv exists in the same directory
    skincare_responses = read_dataset(dataset_file)
    response = skincare_chatbot(user_input, skincare_responses)
    return response

if __name__ == '__main__':
    app.run(debug=True)
