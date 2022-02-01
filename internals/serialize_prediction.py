from functools import reduce

from lo.get import get

def update_list(acc, scores, label):
    acc[0].append({'label': label, 'score': scores[acc[1] + 1]})
    return acc[0]

def label_reducer(scores):
    return lambda acc,l: [update_list(acc, scores, l), acc[1] + 1]

def serialize_prediction(prediction):
    has_labels = isinstance(get(prediction, "labels", None), list)
    has_scores = isinstance(get(prediction, "scores", None), list)
    if has_labels and has_scores:
        scores = prediction["scores"]
        result = reduce(
            label_reducer(scores),
            prediction['labels'],
            [[], -1]
        )
        return result[0]
    json_dict = {
        "label": get(prediction, "label", None),
        "score": get(prediction, "score", None),
        "start": get(prediction, "start", None),
        "end": get(prediction, "end", None),
        "answer": get(prediction, "answer", None),
    }
    return [json_dict]