FROM python:3.9.5-alpine3.13

#RUN apt-get update
#RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y

ADD . /

WORKDIR /

ADD requirements.txt /
ADD run_server.sh /
RUN pip3 install --no-cache-dir -r requirements.txt


CMD [ "sh", "./run_server.sh" ]