from flask import Flask, jsonify, request
import json
import os

from models.predict import predict

app = Flask(__name__)

def serialize_prediction(prediction):
    json_dict = {
        "score": prediction["score"],
        "start": prediction["start"],
        "end": prediction["end"],
        "answer": prediction["answer"]
    }
    return json_dict

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
    query = body['query']
    # json_res = serialize_doc(doc, matches)
    options = body['options'] if body['options'] else {}
    predictions = predict(model, context, query, options = options)
    print('pred', predictions)
    json_predictions = list(map(serialize_prediction, predictions))
    payload = {'predictions': predictions}
    print('payload', payload)
    return jsonify(payload)

if __name__ == '__main__':
    app.run(
        debug=os.environ.get('DEBUG', False) == 'True',
        port=os.environ.get('PORT', 5001), 
        host=os.environ.get('HOST', '127.0.0.1')
    )