# # The Pegasus model is designed for abstractive summarization
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("google/pegasus-large")

# model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-large")

# def predict(context):
#   predictions = model(context)
#   return predictions