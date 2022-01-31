from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# paragraph = "Doctor: What brings you in today? Patient: I have a severe headache. The reason for the patient's visit is"

def predict(context, query, options):
  max_length = options['max_length'] if options['max_length'] else 100
  predictions = model(context, max_length=max_length)
  return predictions
