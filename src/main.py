from flask import Flask, render_template_string, request
from graph import graph

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Company Information Search</title>
    <style>
        body { margin: 40px; font-family: Arial, sans-serif; }
        .container { max-width: 800px; margin: 0 auto; }
        input[type=text] { width: 100%; padding: 12px 20px; margin: 8px 0; }
        button { padding: 12px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button:disabled { background-color: #cccccc; cursor: not-allowed; }
        .results { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Company Information Search</h1>
        <form method="POST" onsubmit="handleSubmit(event)">
            <input type="text" name="url" placeholder="Enter company website URL" value="https://www.example.com">
            <button type="submit" id="searchButton">Search</button>
        </form>
        {% if results %}
        <div class="results">
            <h2>Company Information Report</h2>
            <ol>
                <li><strong>Public or Private Company:</strong> {{ results[0] }}</li>
                <li><strong>CNPJ:</strong> {{ results[1] }}</li>
                <li><strong>Annual Revenue:</strong> {{ results[2] }}</li>
                <li><strong>Industry/Market:</strong> {{ results[3] }}</li>
                <li><strong>Number of Employees:</strong> {{ results[4] }}</li>
                <li><strong>Employee Satisfaction Index:</strong> {{ results[5] }}</li>
                <li><strong>Business Model:</strong> {{ results[6] }}</li>
                <li><strong>Main Products and Services:</strong> {{ results[7] }}</li>
                <li><strong>Supply Chain / Main Suppliers:</strong> {{ results[8] }}</li>
            </ol>
        </div>
        {% endif %}
    </div>

    <script>
        function handleSubmit(event) {
            const button = document.getElementById('searchButton');
            button.disabled = true;
            button.innerHTML = 'Searching...';
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def main():
    results = None
    if request.method == "POST":
        url = request.form.get("url")
        input_state = {
            "url": url,
            "targets": [
                "Determine if the company is publicly traded or privately held",
                "Find the company's official CNPJ (Brazilian corporate tax ID number)",
                "Retrieve the company's annual revenue or financial turnover figures",
                "Identify the industry sector or market in which the company operates",
                "Find the total number of employees currently working at the company",
                "Look up employee satisfaction ratings or internal workplace reviews",
                "Understand the company's business model, including how it generates and captures value",
                "List the company's main products and services offered to consumers or businesses",
                "Identify key suppliers or details about the company's supply chain operations"
            ]
        }
        result = graph.invoke(input_state)
        results = result['answers']
    
    return render_template_string(HTML_TEMPLATE, results=results)

if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=8000)