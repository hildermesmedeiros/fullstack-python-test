FROM alpine
FROM python:3.6

LABEL maintainer="Hildermes José Medeiros Filho <hildermes@gmail.com>"

EXPOSE 5000

# COPY source  destination
WORKDIR /app

COPY requirements.txt /app

RUN pip3.6 install --requirement /app/requirements.txt

#COPY app.py /app
# docker commands is from to
# so from folder build, '.' to folder app, '/app'
#add just to remember I might need it some day to use links or tar files, zip, etc.  
ADD . /app
#COPY testes.py /app
#COPY static /app/static
#COPY static/css /app/static/css
#COPY static/images /app/static/images
#COPY templates /app/templates
#COPY backEnd /app/backEnd

#CMD ["python","-u", "app.py"]
CMD python testes.py
