from transformers import pipeline

model = pipeline(
  'fill-mask',
  model='roberta-base',
  tokenizer='roberta-base'
)

def predict(context, query, options = {}):
  if not query:
    print('query is required for MLM model')
    return list()
  # replace normal mask with the special version required for this model...
  parsed_query = query.replace('[MASK]', '<mask>')
  predictions = [model(parsed_query)]
  return predictions
