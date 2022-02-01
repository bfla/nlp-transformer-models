from transformers import pipeline

model = pipeline(
  'zero-shot-classification',
  model='facebook/bart-large-mnli',
  tokenizer='facebook/bart-large-mnli'
)

# in this case, context is the candidate labels
# query is the string to be analyzed
def predict(context, query, options = {}):
  if not context or not isinstance(context, list):
    return list([{'error': 'context (a list of topics) is required for one-shot classifier'}])
  if not query:
    return list([{'error': 'query is required for MLM model'}])
  if len(context) > 10:
    return list([{'error': 'context (list of topics) must be 10 or fewer items long'}])
  predictions = [model(query, context)]
  return predictions
