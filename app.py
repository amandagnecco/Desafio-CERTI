from flask import Flask, request, jsonify
from moduloextenso import funcextenso
import json



app = Flask(__name__)

@app.route('/<name>', methods=['GET', 'POST'])
def my_view_func(name):
#    return name
    n = name
    jsonContent = {
        "extenso": funcextenso(int(n)),
    }

    outputJson = json.dumps(jsonContent)
    
    return outputJson
#    return jsonify(extenso=funcextenso(int(n)))

if __name__ == "__main__":
    app.run(debug=True)
