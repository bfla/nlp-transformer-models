from transformers import pipeline

model = pipeline(
  'fill-mask',
  model='NLP4H/ms_bert',
  tokenizer='NLP4H/ms_bert'
)

def predict(context, query, options = {}):
  if not query:
    print('query is required for MLM model')
    return list()
  predictions = [model(query)]
  return predictions
