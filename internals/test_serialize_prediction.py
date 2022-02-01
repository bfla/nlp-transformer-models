# from types import SimpleNamespace
from internals.serialize_prediction import serialize_prediction

def test_serialize_prediction_from_qa_pipeline():
    prediction = {
        "answer": 'Brian',
        "start": 5,
        "end": 10,
        "score": 0.24,
    }
    actual = serialize_prediction(prediction)
    assert type(actual) == list
    assert type(actual[0]) == dict
    assert actual[0]["answer"] == 'Brian'
    assert actual[0]["start"] == 5
    assert actual[0]["end"] == 10
    assert actual[0]["score"] == 0.24

def test_serialize_prediction_from_oneshot_pipeline():
    # prediction = SimpleNamespace()
    prediction = {
        "scores": [0.24, 0.85, 0.46],
        "labels": ['hpiQuality', 'hpiSeverity', 'hpiOnset'],
    }
    assert type(prediction["scores"]) == list
    assert type(prediction["labels"]) == list
    actual = serialize_prediction(prediction)
    expected = [
        {"label": "hpiQuality", "score": 0.24},
        {"label": "hpiSeverity", "score": 0.85},
        {"label": "hpiOnset", "score": 0.46}
    ]
    assert type(actual) == list
    assert actual == expected