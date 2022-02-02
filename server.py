from flask import Flask, jsonify, request
import json
import os

from lo.get import get
from lo.flatten import flatten
from lo.fmap import fmap
from lo.pipe import pipe
from internals.serialize_prediction import serialize_prediction
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
    model = get(body, 'model', None)
    # if not model:
    context = get(body, 'context', None)
    query = get(body, 'query', None)
    options = get(body, 'options', {})
    predictions = predict(model, context, query, options = options)
    print('pred', predictions)
    json_predictions = pipe(
        fmap(serialize_prediction),
        flatten(1)
    )(predictions)
    payload = {'predictions': json_predictions}
    print('payload', payload)
    return jsonify(payload)

if __name__ == '__main__':
    app.run(
        debug=os.environ.get('DEBUG', False) == 'True',
        port=os.environ.get('PORT', 5001), 
        host=os.environ.get('HOST', '127.0.0.1')
    )