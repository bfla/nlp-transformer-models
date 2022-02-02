from transformers import pipeline

# from lib.parse_option import parse_option

# from transformers import AutoTokenizer, AutoModelForTokenClassification

# tokenizer = AutoTokenizer.from_pretrained("sciarrilli/biobert-base-cased-v1.2-finetuned-ner")

# model = AutoModelForTokenClassification.from_pretrained("sciarrilli/biobert-base-cased-v1.2-finetuned-ner")
# model.eval()

# This model is trained to pull out disease names and chemicals (drugs)
model = pipeline(
  'ner',
  model='alvaroalon2/biobert_diseases_ner',
  tokenizer='alvaroalon2/biobert_diseases_ner'
)

def predict(context, query, options = {}):
  if not context:
    print('context is required for NER pipeline')
    return []
  # max_length = parse_option(options, 'max_length', 100)
  # embeddings = tokenizer.encode(context, return_tensors='pt')
  predictions = model(context)
  print('biobert_ner.predictions', predictions)
  return predictions