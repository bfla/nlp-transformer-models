# question-answering extractive models
# import models.albert_qa_extractive
# import models.bert_qa_extractive
# import models.biobert_qa_extractive
# import models.roberta_qa_extractive
import models.distilbert_qa_extractive
# import models.electra_qa_extractive
# question-answering yes-no models
import models.roberta_base_qa_yn
# NER models
# import models.biobert_ner
# MLM models
import models.bertbase_mlm
# import models.msbert_mlm
# import models.roberta_mlm
# GPT models
import models.distilgpt2
# import models.gptj
# One-shot classifiers
# import models.fbbart_oneshot
# Abstractive summarization models
# import models.pegasus_large

models = {
    # BERT QA models
    # "albert_qa_extractive": models.albert_qa_extractive,
    # "bert_qa_extractive": models.bert_qa_extractive, # good
    # "biobert_qa_extractive": models.biobert_qa_extractive, # good
    # "roberta_qa_extractive": models.roberta_qa_extractive, # good
    "distilbert_qa_extractive": models.distilbert_qa_extractive,
    # Y/N QA models:
    # https://medium.com/illuin/deep-learning-has-almost-all-the-answers-yes-no-question-answering-with-transformers-223bebb70189
    "roberta_base_qa_yn": models.roberta_base_qa_yn,
    # Fill-mask models:
    "bertbase_mlm": models.bertbase_mlm, # good
    # "msbert_mlm": models.msbert_mlm, # poor
    # "roberta_mlm": models.roberta_mlm, # good
    # One-shot classifiers
    # "fbbart_oneshot": models.fbbart_oneshot, # good
    # "biobert_mml": ,
    # "bluebert_mml": ,
    # "electra_qa_extractive": models.electra_qa_extractive,
    # NER models
    # "biobert_ner": models.biobert_ner,
    # GPT models
    "distilgpt2": models.distilgpt2,
    # "gpt2_large": models.gpt2_large,
    # "gpt2_xl": models.gpt2_xl,
    # "gptj": gptj,
    # "gptneo": gptneo,
    # Abstractive summarization
    # "pegasus_large": pegasus_large
}

default_options = {
  
}

# should return a list of predictions
def predict(model, context, query, options = default_options):
    model = models[f"{model}"]
    if not model:
        return list()
    predictions = model.predict(context, query, options = options)
    return predictions