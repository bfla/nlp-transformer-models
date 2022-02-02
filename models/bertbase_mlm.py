from transformers import pipeline

model = pipeline(
  'fill-mask',
  model='bert-base-uncased',
  tokenizer='bert-base-uncased'
)

def predict(context, query, options = {}):
  if not query:
    print('query is required for MLM model')
    return list()
  predictions = [model(query)]
  return predictions