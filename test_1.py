from bs4 import BeautifulSoup
import requests
from googlesearch import search
import json
from flask import Flask, request, jsonify, send_from_directory
import openai
from dotenv import load_dotenv

load_dotenv()
import os

api_key = os.environ.get("OPENAI_API_KEY")
app = Flask(__name__)

def generate_summary(data):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following information in 150 words:\n{data}",
    )
    return response.choices[0].text.strip()

@app.route('/api/search', methods=['GET'])
def search_api():
    query = request.args.get('query')
    all_data = []

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        data = requests.get(j)
        soup1 = BeautifulSoup(data.text, 'html.parser')
        title = soup1.find('h1')

        if 'twitter.com' in j:
            print(f"Ignoring Twitter URL: {j}")
            continue

        if title:
            title = title.text.strip()
            paras = soup1.find_all('p')

            if paras:
                paras_comb = '\n'.join(para.text.strip() for para in paras)
                link_data = {'title': title, 'url': j, 'content': paras_comb}
                all_data.append(link_data)
            else:
                print("No paragraphs found.")
        else:
            print(f"No h1 tag found on {j}")

    json_data = json.dumps(all_data, indent=2)
    summary_text = generate_summary(json_data)
    return jsonify({'summary': summary_text})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'static/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '_main_':
    app.run(debug=True)