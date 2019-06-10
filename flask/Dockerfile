FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

# Install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt

RUN pip install --upgrade google-api-python-client
RUN pip install google-cloud-storage

ADD app.py .
ADD cars_meta.csv .
ADD model ./model
CMD [ "python", "app.py" ]i
