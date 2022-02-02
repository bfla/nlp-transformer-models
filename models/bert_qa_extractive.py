from transformers import pipeline

model = pipeline(
  'question-answering',
  model='bert-large-cased-whole-word-masking-finetuned-squad',
  tokenizer='bert-large-cased-whole-word-masking-finetuned-squad'
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
  
# paragraph = 'A new study estimates that if the US had universally mandated masks on 1 April, there could have been nearly 40% fewer deaths by the s

# answer_0 = predict({'question': 'What is this article about?','context': f'{paragraph}'})
# print(answer_0)

# answer_1 = predict({'question': 'Which country is this article about?',
#            'context': f'{paragraph}'})
# print(answer_1)

# answer_2 = predict({'question': 'Which disease is discussed in this article?',
#            'context': f'{paragraph}'})
# print(answer_2)

# answer_3 = predict({'question': 'What time period is discussed in the article?',
#            'context': f'{paragraph}'})
# print(answer_3)
