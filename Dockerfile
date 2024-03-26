
FROM python

ENV REDIS_CONNECT=${REDIS_CONNECT}
ENV DATA_FOLDER=/data
ENV LOG_FOLDER=/var/log
RUN apt-get update && apt-get -y install cron


WORKDIR /failsafe_cron

COPY app app
COPY main.py .
COPY requirements.txt .
COPY --chmod=0755 scripts/start_cron.sh start_cron.sh

RUN pip install -r requirements.txt
RUN ./start_cron.sh



CMD ["/bin/bash", "-c", "cron && tail -f /var/log/cron.log"]
