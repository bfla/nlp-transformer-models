from flask import Flask, jsonify, request
import json
import os

from models.predict import predict

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    json_res = {
        'status': 'healthy'
    }
    return jsonify(json_res)

@app.route('/pipelines', methods=['POST'])
def post_pipelines():
    # print(request)
    body = request.json
    model = body['model']
    context = body['context']
    # json_res = serialize_doc(doc, matches)
    predictions = predict(model, context, options)
    json_res = jsonify({'predictions': predictions})
    return jsonify(json_res)

if __name__ == '__main__':
    app.run(
        debug=os.environ.get('DEBUG', False) == 'True',
        port=os.environ.get('PORT', 5001), 
        host=os.environ.get('HOST', '127.0.0.1')
    )