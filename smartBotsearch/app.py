from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load AI tools data from JSON file
with open('ai_tools.json', 'r') as f:
    ai_tools = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', tools=ai_tools[:20])  # Show first 20 on homepage

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '').lower()
    pricing = request.args.get('pricing', '').lower()
    
    results = []
    
    for tool in ai_tools:
        matches_query = (query in tool['name'].lower() or 
                query in tool['function'].lower()) 
        
        matches_category = (not category or 
                           category in [c.lower() for c in tool['categories']])
        
        matches_pricing = (not pricing or 
                          pricing == tool['pricing'].lower())
        
        if matches_query and matches_category and matches_pricing:
            results.append(tool)
    
    return render_template('search.html', tools=results, query=query)

@app.route('/api/tools')
def api_tools():
    query = request.args.get('q', '').lower()
    limit = int(request.args.get('limit', 5))
    
    suggestions = []
    for tool in ai_tools:
        if query in tool['name'].lower():
            suggestions.append({
                'name': tool['name'],
                'function': tool['function']
            })
            if len(suggestions) >= limit:
                break
    
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)