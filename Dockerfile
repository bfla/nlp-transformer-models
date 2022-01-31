FROM python:3.7

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install packages next to reduce size of layers that need to be rebuilt
# whenever source files are
COPY ./server.py /usr/src/app/server.py
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN python --version
RUN pip install -r requirements.txt
RUN python -m spacy download en
RUN echo '[]' > patterns.json

ENV HOST 0.0.0.0
ENV PORT 5000

COPY ./patterns.json /data/patterns.json

# Bundle app source
# RUN mkdir -p /usr/src/app/build
# COPY ./build /usr/src/app/build
# COPY ./ /usr/src/app/

CMD ["python", "server.py"]
