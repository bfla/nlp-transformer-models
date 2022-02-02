# https://huggingface.co/shahrukhx01/roberta-base-boolq
import torch
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForSequenceClassification.from_pretrained("shahrukhx01/roberta-base-boolq")
model.to(device)

tokenizer = AutoTokenizer.from_pretrained("shahrukhx01/roberta-base-boolq")

def predict(context, query, options = {}):
  sequence = tokenizer.encode_plus(query, context, return_tensors="pt")['input_ids'].to(device)
  
  logits = model(sequence)[0]
  probabilities = torch.softmax(logits, dim=1).detach().cpu().tolist()[0]
  proba_yes = round(probabilities[1], 2)
  proba_no = round(probabilities[0], 2)
  prediction = {
    "labels": ["yes", "no"],
    "scores": [proba_yes, proba_no]
  }
  return [prediction]

  # print(f"Question: {question}, Yes: {proba_yes}, No: {proba_no}")
  
# passage = """Berlin is the capital and largest city of Germany by both area and population. Its 3.8 million inhabitants make it the European Union's most populous city, 
#                         according to population within city limits."""
 
# question = "Is Berlin the smallest city of Germany?"
# predict(s_question, passage)