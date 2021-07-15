from flask import Flask, render_template,request,jsonify
from main import FetchJob


app = Flask(__name__)

@app.route('/api/v1/resources/technology', methods=['GET'])
def api_id():
    name = request.args['name']
    result = FetchJob(name)
    
    return(jsonify(result))

if __name__ == "__main__":
    app.run()

