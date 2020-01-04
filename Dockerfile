FROM python:alpine3.7
COPY . /
WORKDIR /application_events
RUN pip3 install -r requirements.txt
EXPOSE 10000
CMD python3 -u ./event_service.py
