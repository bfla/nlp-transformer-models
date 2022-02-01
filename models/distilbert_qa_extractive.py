from transformers import pipeline

model = pipeline(
  'question-answering',
  model='distilbert-base-cased-distilled-squad',
  tokenizer='distilbert-base-cased-distilled-squad'
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