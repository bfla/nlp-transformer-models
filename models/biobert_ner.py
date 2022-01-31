from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("sciarrilli/biobert-base-cased-v1.2-finetuned-ner")

model = AutoModelForTokenClassification.from_pretrained("sciarrilli/biobert-base-cased-v1.2-finetuned-ner")

def predict(context, query, options):
  predictions = model(context)
  return predictions