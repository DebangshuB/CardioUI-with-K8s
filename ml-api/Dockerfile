FROM python:3.8.7-slim-buster

WORKDIR .

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD ["gunicorn"  , "-b", "0.0.0.0:8001", "app:app"]