#build command
#docker build -t hunterofshadows/voter.review:v1 .

#run command
#docker run -d --rm --name voter.review hunterofshadows/voter.review:v1


FROM python:3.9-buster

#WORKDIR /usr/src/app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir wget

RUN apt-get update && \
	apt-get upgrade -y