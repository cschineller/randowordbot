FROM python:3.7-alpine

COPY config.py /bots/
COPY randowords.py /bots/
COPY postword.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install random_word
RUN pip3 install PyDictionary
RUN pip3 install pyyaml

WORKDIR /bots
ENV PYTHONPATH /venv
CMD ["python3", "postword.py"]