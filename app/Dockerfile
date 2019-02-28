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
#ADD is similar do COPY, metal note: remember I might need it some day, use it with links or tar files, zip, etc. 
 
ADD . /app 
RUN chmod +x /app/start.sh
CMD ["./start.sh"]
