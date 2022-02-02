from transformers import pipeline

model = pipeline(
  'question-answering',
  model='mfeb/albert-xxlarge-v2-squad2',
  tokenizer='mfeb/albert-xxlarge-v2-squad2'
)

def predict(context, query, options = {}):
  if not context:
    print('context is required for question-answering model')
    return list()
  if not query:
    print('query is required for question-answering model')
    return list()
  params = {
    'context': context,
    'question': query
  }
  predictions = [model(params)]
  return predictions