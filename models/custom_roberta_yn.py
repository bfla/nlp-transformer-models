# See https://medium.com/illuin/deep-learning-has-almost-all-the-answers-yes-no-question-answering-with-transformers-223bebb70189
# https://arxiv.org/abs/1905.10044
import random
import torch
import numpy as np
import pandas as pd
from google.cloud import storage
from tqdm import tqdm
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW

def download_training_data(
    train_path_out = './train.jsonl',
    dev_path_out = './dev.jsonl'):
    # download the training data
    # See: https://www.thecodebuzz.com/python-upload-files-download-files-google-cloud-storage/
    storage_client = storage.Client()
    bucket = storage_client.bucket('boolq')
    blob_train = bucket.blob('train.jsonl')
    blob_train.download_to_filename(train_path_out)
    blob_dev = bucket.blob('dev.jsonl')
    blob_dev.download_to_filename(dev_path_out)

def encode_data(tokenizer, questions, passages, max_length):
    """Encode the question/passage pairs into features than can be fed to the model."""
    input_ids = []
    attention_masks = []

    for question, passage in zip(questions, passages):
        encoded_data = tokenizer.encode_plus(question, passage, max_length=max_length, pad_to_max_length=True, truncation_strategy="longest_first")
        encoded_pair = encoded_data["input_ids"]
        attention_mask = encoded_data["attention_mask"]

        input_ids.append(encoded_pair)
        attention_masks.append(attention_mask)

    return np.array(input_ids), np.array(attention_masks)

def train(
    model_variant='roberta-base', 
    train_path = './train.jsonl', 
    dev_path = './dev.json.l'):
    # Use a GPU if you have one available (Runtime -> Change runtime type -> GPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Set seeds for reproducibility
    random.seed(26)
    np.random.seed(26)
    torch.manual_seed(26)

    # configure tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_variant) 
    model = AutoModelForSequenceClassification.from_pretrained(model_variant)
    model.to(device) # Send the model to the GPU if we have one
    learning_rate = 1e-5 # same as the BoolQ paper
    optimizer = AdamW(model.parameters(), lr=learning_rate, eps=1e-8)

    # Load data
    download_training_data(train_path_out=train_path_out,dev_path_out=dev_path_out)
    train_data_df = pd.read_json(train_path, lines=True, orient='records')
    dev_data_df = pd.read_json(dev_path, lines=True, orient="records")

    passages_train = train_data_df.passage.values
    questions_train = train_data_df.question.values
    answers_train = train_data_df.answer.values.astype(int)

    passages_dev = dev_data_df.passage.values
    questions_dev = dev_data_df.question.values
    answers_dev = dev_data_df.answer.values.astype(int)

    # Encoding data
    max_seq_length = 256
    input_ids_train, attention_masks_train = encode_data(tokenizer, questions_train, passages_train, max_seq_length)
    input_ids_dev, attention_masks_dev = encode_data(tokenizer, questions_dev, passages_dev, max_seq_length)
    train_features = (input_ids_train, attention_masks_train, answers_train)
    dev_features = (input_ids_dev, attention_masks_dev, answers_dev)

    # Building Dataloaders
    batch_size = 32

    train_features_tensors = [torch.tensor(feature, dtype=torch.long) for feature in train_features]
    dev_features_tensors = [torch.tensor(feature, dtype=torch.long) for feature in dev_features]

    train_dataset = TensorDataset(*train_features_tensors)
    dev_dataset = TensorDataset(*dev_features_tensors)

    train_sampler = RandomSampler(train_dataset)
    dev_sampler = SequentialSampler(dev_dataset)

    train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=batch_size)
    dev_dataloader = DataLoader(dev_dataset, sampler=dev_sampler, batch_size=batch_size)

