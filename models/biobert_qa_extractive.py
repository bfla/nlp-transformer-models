from transformers import pipeline

model = pipeline(
  'question-answering',
  model='dmis-lab/biobert-large-cased-v1.1-squad',
  tokenizer='dmis-lab/biobert-large-cased-v1.1-squad'
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