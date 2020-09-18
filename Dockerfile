FROM python:3.7.2
WORKDIR /app
COPY ./src /app
RUN pip install --default-timeout=1000 -r requirements.txt
RUN apt-get update && apt-get install -q -y vim && \
    apt-get install -y cmake build-essential && \
    apt-get install -y tcpdump && \
    apt-get install -y gdb

    
#RUN chmod +x setup.sh

#ENTRYPOINT ["bash" ,"setup.sh"]
CMD ["uwsgi", "app.ini"]


