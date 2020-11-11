#build command
#docker build -t hunterofshadows/voter.review:v1 .

#run command
#docker run -d --rm --name voter.review hunterofshadows/voter.review:v1


FROM python:rc-buster

#WORKDIR /usr/src/app

COPY requirements.txt ./
COPY pull.stats.py ./
COPY updateBtn.py ./
COPY pull.stats.v2.py ./
COPY pull.stats.test.py ./
COPY ./google.sheets/codCredentials.json ./google.sheets/codCredentials.json

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
	apt-get upgrade -y