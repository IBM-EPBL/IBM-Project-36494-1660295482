import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":" Web Developer , USA","num_pages":"1"}

headers = {
	"X-RapidAPI-Key": "d118e88785mshb0e33767fd34476p166ed9jsna896a9c9e5da",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}



@app.route("/", methods=['GET'])
def api():
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data

    # {% for datas in data[job_apply_link] %}


if __name__ == "__main__":
    app.run(debug=True, port=5333)