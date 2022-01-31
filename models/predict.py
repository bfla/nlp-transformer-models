import models.bert_qa_extractive
import models.biobert_ner
import models.distilgpt2
# import models.gptj
# import models.pegasus_large

models = {
    "bert_qa_extractive": models.bert_qa_extractive,
    "biobert_ner": models.biobert_ner,
    "distilgpt2": models.distilgpt2,
    # "gptj": gptj,
    # "pegasus_large": pegasus_large
}

default_options = {
  
}

# should return a list of predictions
def predict(model, context, query, options = default_options):
    model = models[f"{model}"]
    if not model:
        return list()
    predictions = model.predict(context, query, options)
    return predictions