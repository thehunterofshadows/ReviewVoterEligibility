#build command
#docker build -t hunterofshadows/voter.review:v1 .

#run command
#docker run -d --rm --name voter.review hunterofshadows/voter.review:v1


FROM python:rc-buster

#WORKDIR /usr/src/app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
	apt-get upgrade -y