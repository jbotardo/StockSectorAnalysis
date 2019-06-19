from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/performance', methods=["POST"])
def performance():
    sector = request.form['sector']
    r = requests.get('https://www.alphavantage.co/query?function='+sector+',&apikey=DIH7DPEEI0O1P4FW')
    json_object = r.text
    return json_object
    # return render_template('sector.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)