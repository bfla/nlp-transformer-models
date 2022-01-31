# spacy-core-api
This project is a light HTTP API wrapper around the spacy toolkit (for natural language processing).  

You can send requests containing strings and get output from spacy including named entities and part-of-speech tags.

You generally don't need this code unless you plan on making changes to the underlying API.  In most cases, you can simply run it in a Docker container: `buccaneerai/spacy-api:latest`.

## Dependencies
As usual, Python is extremely fussy about using exactly the right version:
- Python 3.7

## Setup the project locally
```bash
# create a virtual environment (with Python 3.7)
python -m venv ./env

# use the virtual environment
source ./env/bin/activate

# Install packages
python install -r ./requirements.txt
```

## Useful commands
```bash
# use the virtual environment:
source ./env/bin/activate

# run the app (on port 5000)
DEBUG=True python3 ./server.py

# to install all packages:
pip3 install -r .requirements.txt

# to freeze packages
pip3 freeze > .requirements.txt

# to install a new package:
pip3 install my_package && pip freeze > ./requirements.txt
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
  --data '{"model":"distilgpt2","context":"Hello. My name is Fido.  I am a Dog.  How are you today?"}' \
  http://localhost:5001/pipeline
```