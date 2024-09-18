from flask import Flask, render_template, request, jsonify
# from serpapi import GoogleSearch
import serpapi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_results = perform_search_with_serpapi(data['category'], data['keyword'])
    return jsonify(search_results)

def perform_search_with_serpapi(category, keyword):
    params = {
        "engine": "google_scholar",
        "q": keyword,
        "api_key": "aa334813c264cc49eaeb2febf86e2da445c81ebd3ed8c403d121dc841f9fc93e"
    }
    results = serpapi.search(params)
    # print("Search results: ", search)
    organic_results = results.get('organic_results', [])
    return organic_results[:5]  # Return top 5 results

if __name__ == '__main__':
    app.run(debug=True)
