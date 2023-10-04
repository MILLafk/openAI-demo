import openai
from flask import Flask, render_template, request

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response_text = ""

    if request.method == 'POST':
        user_prompt = request.form['user_prompt']

        # Make an API request to generate text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_prompt,
            max_tokens=500,
            temperature=0.1,
            n=2,
            stop=None
        )

        # Extract the response text
        response_text = response.choices[0].text.strip()

    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)