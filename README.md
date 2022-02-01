# nlp-transformer-models
This project is a light HTTP API wrapper around Hugging Face NLP transformers.

## Dependencies
As usual, Python is extremely fussy about using exactly the right version:
- Python 3.9

## Setup the project locally
You'll need to have `pipenv` installed.  To install it:
```bash
# install the pipenv package manager
pip install pipenv
# or
pip3 install pipenv
```
Now you can install this project's dependencies:
```bash
# Install packages
pipenv install --dev
```

> 💡 The first time you run the server, it will need to download any models that aren't stored on the local machine.  These models are large and it may take some time.

## Useful commands
```bash
# use the virtual environment:
# source ./.env/bin/activate
pipenv shell

# run the app (on port 5001)
DEBUG=True pipenv run python ./server.py

# run tests
# pipenv run python -m test
pipenv run pytest

# to install a new package:
pipenv install my_package
```

## Environment variables (optional)
- `PORT`: Defaults to `5001`.
- `HOST`: Defaults to `0.0.0.0`.
- `DEBUG` (optional): Run Flask server in debug mode. Set to 'True' if desired.

## Running the Docker Container
> 💡 Check out our devops repository. It has a docker-compose file that lets you run the container.

## HTTP API

### `POST /pipeline`
Gets tokens (including part-of-speech tags and named entities) from a given string.
```bash
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"model":"distilbert_qa_extractive","context":"Hello. My name is Fido.  I am a Dog.  How are you today?","query": "Is Fido a human or a dog?"}' \
  http://localhost:5001/pipeline
```