from transformers import pipeline

model = pipeline(
  'question-answering',
  model='ahotrod/electra_large_discriminator_squad2_512',
  tokenizer='ahotrod/electra_large_discriminator_squad2_512'
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