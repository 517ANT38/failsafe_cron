
FROM python


ENV DATA_FOLDER=/data
ENV LOG_FOLDER=/var/log
RUN apt-get update && apt-get -y install cron


WORKDIR /failsafe_cron

COPY app app
COPY main.py .
COPY requirements.txt .
COPY --chmod=0755 scripts/create_cmd.sh .

RUN pip install -r requirements.txt
RUN mkfifo --mode 0666 /var/log/cron.log
RUN mkdir /data

CMD  ./create_cmd.sh && cron && tail -f /var/log/cron.log
