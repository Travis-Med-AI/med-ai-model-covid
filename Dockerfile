FROM ai-model:latest as model
# FROM tensorflow/tensorflow:2.0.0-py3
FROM python:3.8
WORKDIR /opt

# Install Dependencies
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

# DONT EDIT THIS SECTION
# add current directory to container
RUN pip install redis scikit-image
COPY --from=model /opt/runner /opt
ADD . /opt/
CMD python runner.py

# CMD python3 main.py
