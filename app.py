from flask import Flask, redirect, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=69a12cdc3b3145339c44c74575403062"
    r = requests.get(url).json()

    cases = {
        'articles' : r['articles']
    }
    return render_template('index.html', case = cases)









if __name__ == "__main__":
    app.run(debug=True)