from flask import Flask, request, redirect
import urllib.request

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    if url.startswith("https://ul.edu.lb"):
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    return redirect('/')