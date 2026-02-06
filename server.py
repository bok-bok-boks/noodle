from flask import send_file, Flask, request, render_template
from ddgs import DDGS
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('html/index.html')

def searchResults(query):
    results = DDGS().text(query, max_results=50, backend="google")

    return results

def imgSearchResults(query):
    results = DDGS().images(query, max_results=50, backend="google")

    return results

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return send_file('html/search_failure.html')
    
    q = request.form.get("query")

    return render_template('search.html', title=q, results=searchResults(q))
    
@app.route('/imgSearch', methods=["GET", "POST"])
def searchImg():
    if request.method == "GET":
        return send_file('html/search_failure.html')
    
    q = request.form.get("query")

    return render_template('searchImg.html', title=q, results=imgSearchResults(q))
    
if (__name__ == "__main__"):
    app.run("0.0.0.0", 80)