FROM python:3
COPY . /
WORKDIR /edi
RUN apt-get update && apt-get -y install gcc && echo
RUN pip3 install -r requirements.txt
CMD python3 -u ./event_consumer.py >> event.log & python3 -u ./remediation.py >> remediation.log