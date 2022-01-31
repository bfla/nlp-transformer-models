# TENSORFLOW IMPLEMENTATION =======================================================
# https://towardsdatascience.com/how-you-can-use-gpt-j-9c4299dd8526
# from transformers import GPTJForCausalLM
# import tensorflow

# model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", revision="float16", torch_dtype=tf.float16, low_cpu_mem_usage=True)
# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
# context = """In a shocking finding, scientists discovered a herd of unicorns living in a remote, 
#           previously unexplored valley, in the Andes Mountains. Even more surprising to the 
#           researchers was the fact that the unicorns spoke perfect English."""

# input_ids = tokenizer(context, return_tensors="tf").input_ids
# gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=100,)
# gen_text = tokenizer.batch_decode(gen_tokens)[0]
# print(gen_text)

# PYTORCH IMPLEMENTATION =======================================================
# https://towardsdatascience.com/how-you-can-use-gpt-j-9c4299dd8526
# https://huggingface.co/docs/transformers/master/model_doc/gptj
# from transformers import GPTJForCausalLM
# import torch

# def load_model():
#   model = GPTJForCausalLM.from_pretrained(
#     "EleutherAI/gpt-j-6B", 
#     revision="float16", 
#     torch_dtype=torch.float16, 
#     low_cpu_mem_usage=True
#   )
#   return model

# def tokenize(context):
#   tokenizer = 

# TRANSFORMERS LIBRARY IMPLEMENTATION ==========================================
# from transformers import pipeline

# model = pipeline('text-generation', model='EleutherAI/gpt-j-6B')

# paragraph = "Doctor: What brings you in today? Patient: I have a severe headache. The reason for the patient's visit is"

# def predict(context, options):
#   max_length = options["max_length"] if options['max_length'] else 100
#   predictions = model(context, max_length = max_length)
#   return predictions
