FROM ubuntu:18.10
FROM python:3.6

LABEL maintainer="Hildermes José Medeiros Filho <hildermes@gmail.com>"

EXPOSE 5000

WORKDIR /app
# COPY source  destination

COPY requirements.txt /app
COPY app.py /app
COPY testes.py /app
COPY static /app/static
COPY static/css /app/static/css
COPY static/images /app/static/images
COPY templates /app/templates
COPY backEnd /app/backEnd

RUN pip3 install -r requirements.txt

#CMD python app.py
CMD python testes.py
